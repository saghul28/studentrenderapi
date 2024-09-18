from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import google.generativeai as genai
import re

router = APIRouter()

# Configure Google GenAI (Remember to set your API key as an environment variable)
genai.configure(api_key=os.getenv("GENAIAPI_KEY"))

# Choose the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Global variables to store generated questions and score
questions_list = {}
current_score = 0
current_question_index = {}

# Models for request data
class QuestionRequest(BaseModel):
    topic: str

class AnswerRequest(BaseModel):
    answer: str
    topic: str  # Added topic to keep track of the session per topic


# Function to generate multiple-choice questions
def generate_questions(topic):
    """Generates assessment questions for the given topic using Gemini Flash."""
    prompt = f"Generate 3 multiple-choice questions related to {topic}. " \
             "Provide 4 answer options for each question, with only one correct answer. " \
             "Format each question as follows:\n" \
             "Question: [Question text]\n" \
             "Options:\n" \
             "A) [Option 1]\n" \
             "B) [Option 2]\n" \
             "C) [Option 3]\n" \
             "D) [Option 4]\n" \
             "Correct Answer: [Letter of the correct answer (A, B, C, or D)]\n\n" \
             "After the correct answer, end with '$$'"

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    questions = response.text.split("$$")
    return questions

def parse_question(question_str):
    """Parses a question string into question text, options, correct answer, and code block."""
    # Initialize variables
    question_text = ""
    options = {}
    correct_answer = ""
    code_block = ""

    # Check if there's a code block
    if '```python' in question_str:
        code_block_match = re.search(r'```python(.*?)```', question_str, re.DOTALL)
        if code_block_match:
            code_block = code_block_match.group(1).strip()
            question_str = question_str.replace(code_block_match.group(0), '')

    # Process remaining question text
    question_lines = question_str.split('\n')
    print(question_lines)
    for line in question_lines:
        line = line.strip()
        if line.startswith('**Question:'):
            question_text = line.split(':', 1)[1].strip()
            print(question_text)
        elif line.startswith('Options'):
            continue  # Skip 'Options' header line
        elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
            letter = line[0]
            option = line[2:].strip()
            options[letter] = option
        elif line.startswith('**Correct Answer'):
            correct_answer = line.split(':** ', 1)[1].strip()

    return question_text, options, correct_answer, code_block

# Function to assess answers using Gemini Flash
def assess_answer(answer, question, code_block):
    """Assesses the student's answer using Gemini Flash."""
    if not question:
        return "Error: Question context is missing."

    prompt = f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n" \
             "Please provide a reason if the answer is correct or incorrect. Keep it short and precise."
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text

# Endpoint to generate questions for a topic
@router.post('/generate_questions')
async def api_generate_questions(request: QuestionRequest):
    global questions_list, current_score, current_question_index
    current_score = 0  # Reset score for a new session
    topic = request.topic

    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required")

    questions = generate_questions(topic)
    if not questions:
        raise HTTPException(status_code=500, detail="Failed to generate questions")

    questions_list[topic] = questions
    current_question_index[topic] = 0  # Start from the first question

    return JSONResponse(content={"message": "Questions generated successfully.", "topic": topic})

# Endpoint to get the next question
@router.get('/next_question')
async def api_next_question(topic: str):
    global questions_list, current_question_index

    if topic not in questions_list or current_question_index.get(topic) is None:
        raise HTTPException(status_code=400, detail="No questions available for the topic or generate questions first.")

    if current_question_index[topic] >= len(questions_list[topic]):
        return JSONResponse(content={"message": "No more questions available."})

    question_text, options, correct_answer, code_block = parse_question(questions_list[topic][current_question_index[topic]])
    
    current_question_index[topic] += 1  # Move to the next question

    return JSONResponse(content={
        "question": question_text,
        "options": options,
        "code_block": code_block
    })

# Endpoint to assess the user's answer and provide feedback
@router.post('/assess_answer')
async def api_assess_answer(answer_request: AnswerRequest):
    global current_score
    answer = answer_request.answer
    topic = answer_request.topic

    if not answer or not topic:
        raise HTTPException(status_code=400, detail="Answer and topic are required")

    if topic not in questions_list or current_question_index.get(topic) is None:
        raise HTTPException(status_code=400, detail="No questions generated for the topic.")

    # Assess the previous question's answer
    question_index = current_question_index[topic] - 1
    question_text, options, correct_answer, code_block = parse_question(questions_list[topic][question_index])
    feedback = assess_answer(answer, question_text, code_block)

    is_correct = "Incorrect" not in feedback or "Incorrect" not in feedback.lower() or feedback.splitlines("**Incorrect")
    if is_correct:
        current_score += 1

    return JSONResponse(content={
        "feedback": feedback,
        "is_correct": is_correct,
        "current_score": current_score
    })
