from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import os
import google.generativeai as genai
import re
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()
router = APIRouter()

# Configure Google GenAI
genai.configure(api_key=os.getenv("GENAI_API_KEY", os.getenv("GENAIAPI_KEY")))

# Choose the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Global variables to manage session state
questions_list = []
current_question_index = 0
current_score = 0

# Data models
class QuestionResponse(BaseModel):
    question: str
    options: dict
    correct_answer: str
    code_block: str = None


class AssessmentRequest(BaseModel):
    topic: str


class SubmitAnswerRequest(BaseModel):
    selected_answer: str
    # code_block:str



class AssessmentResponse(BaseModel):
    feedback: str
    is_correct: bool
    current_score: int
    next_question: QuestionResponse = None


# Function to generate multiple-choice questions
def generate_questions(topic: str):
    """Generates assessment questions for the given topic."""
    prompt = f"Generate 10 multiple-choice questions related to {topic}. Provide 4 answer options for each question, with only one correct answer. Format each question as follows:\nQuestion: [Question text]\nOptions:\nA) [Option 1]\nB) [Option 2]\nC) [Option 3]\nD) [Option 4]\nCorrect Answer: [Letter of the correct answer (A, B, C, or D)]\n\nAfter the correct answer, end with '$$'"

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    questions_text = response.text

    # Split the questions using '$$'
    questions = questions_text.split('$$')

    # Remove any empty entries or whitespace
    questions = [q.strip() for q in questions if q.strip()]
    print(questions)
    return questions


# Function to parse a single question
import re

def parse_questions(response_text: str):
    """Parses multiple questions from a response string."""
    questions = []
    # Split the response by '$$' to get each question individually
    question_strings = response_text.split('$$')

    for question_str in question_strings:
        question_str = question_str.strip()
        if not question_str:
            continue

        # Initialize variables
        question_text = ""
        options = {}
        correct_answer = ""
        code_block = ""

        # Check if there's a code block
        code_block_match = re.search(r'```(?:\w+)?\n(.*?)```', question_str, re.DOTALL)
        if code_block_match:
            code_block = code_block_match.group(1).strip()
            # Remove the code block from the question string
            question_str = re.sub(r'```(?:\w+)?\n(.*?)```', '', question_str, count=1, flags=re.DOTALL).strip()

        # Process remaining question text
        question_lines = question_str.split('\n')
        question_text_found = False
        for line in question_lines:
            line = line.strip()
            if line.startswith('**Question'):
                question_text = line.split(':', 1)[1].strip()
                question_text_found = True
            elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
                letter = line[0]
                option = line[2:].strip()
                options[letter] = option
            elif line.startswith('Correct Answer:'):
                correct_answer = line.split('Correct Answer:', 1)[1].strip()

        if not question_text_found:
            question_text = "No question text found"

        questions.append({
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "code_block": code_block
        })
        print(questions)

    return questions



# Function to assess answers using Gemini Flash
# def assess_answer(question: str, answer: str):
#     """Assesses the student's answer using Gemini Flash."""
#     prompt = (
#         f"Evaluate the following answer for the question: \"{question}\"\n\n"
#         f"Answer: {answer}\n\n"
#         "Respond with 'Correct' if the answer is correct, or 'Incorrect' if the answer is not correct. "
#         "Please provide a brief explanation for your response."
#     )
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     print(response)
#     print(response.text)
#     return response.text
def assess_answer(question: str, selected_option: str, options: dict, correct_answer: str):
    """Assesses the student's selected option for the question using Gemini Flash."""
    # Ensure the option is upper-case
    selected_option = selected_option.upper()

    # Construct the prompt to evaluate the selected option
    prompt = (
        f"Evaluate the following multiple-choice question:\n\n"
        f"Question: \"{question}\"\n\n"
        f"Options:\n"
        f"{', '.join([f'{k}) {v}' for k, v in options.items()])}\n\n"
        f"Selected Option: {selected_option}\n\n"
        f"Correct Answer: {correct_answer}\n\n"
        "Respond with 'Correct' if the selected option is correct, or 'Incorrect' if it is not correct. "
        "Provide a brief explanation for why the selected option is correct or incorrect based on the provided options and the correct answer."
    )

    # Start the chat and send the message
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)

    # Extract and return the text of the response
    response_text = response.text.strip()

    return response_text


# API endpoint to start a new assessment
@router.post("/start-assessment/", response_model=QuestionResponse)
async def start_assessment(request: AssessmentRequest):
    global questions_list, current_question_index, current_score
    current_score = 0
    current_question_index = 0
    questions_list = generate_questions(request.topic)

    if not questions_list:
        raise HTTPException(status_code=404, detail="No questions generated.")

    # Get the first question
    next_question_text = questions_list.pop(0)

    # Parse the question
    parsed_questions = parse_questions(next_question_text)

    if not parsed_questions:
        raise HTTPException(status_code=500, detail="Failed to parse questions.")

    # Assume there is at least one question in parsed_questions
    question_data = parsed_questions[0]
    print(question_data)
    return question_data


# API endpoint to submit an answer and get feedback
@router.post("/submit-answer/", response_model=AssessmentResponse)
async def submit_answer(request: SubmitAnswerRequest):
    global current_question_index, current_score, questions_list

    if current_question_index >= len(questions_list):
        raise HTTPException(status_code=404, detail="No more questions.")

    current_question_text = questions_list[current_question_index]

    # Parse the current question
    parsed_questions = parse_questions(current_question_text)
    current_question = parsed_questions[0]

    # feedback = assess_answer(current_question['question'], request.selected_answer)
    feedback = assess_answer(
        question=current_question['question'],
        selected_option=request.selected_answer,
        options=current_question['options'],
        correct_answer=current_question['correct_answer']
    )

    # Interpret feedback
    # is_correct = feedback.startswith("**Correct") or  feedback.startswith("**Correct")
    is_correct = request.selected_answer.upper() == current_question['correct_answer']

    if is_correct:
        current_score += 1


    current_question_index += 1

    # Get the next question if available
    next_question = None
    if current_question_index < len(questions_list):
        next_question_text = questions_list[current_question_index]
        parsed_questions = parse_questions(next_question_text)
        next_question = parsed_questions[0]

    return {
        "feedback": feedback,
        "is_correct": is_correct,
        "current_score": current_score,
        "next_question": next_question
    }


# API endpoint to get the next question
@router.get("/next-question/", response_model=QuestionResponse)
async def next_question():
    global current_question_index, questions_list

    if current_question_index >= len(questions_list):
        raise HTTPException(status_code=404, detail="No more questions.")

    next_question_text = questions_list[current_question_index]

    # Parse the question
    parsed_questions = parse_questions(next_question_text)
    print(parsed_questions)
    if not parsed_questions:
        raise HTTPException(status_code=500, detail="Failed to parse questions.")

    # Assume there is at least one question in parsed_questions
    question_data = parsed_questions[0]

    return question_data
