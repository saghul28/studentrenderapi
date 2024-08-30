# # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # import os
# # import google.generativeai as genai
# # import random
# # import re
# #
# # app = Flask(__name__)
# # app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')
# #
# # # Configure Google GenAI (Remember to set your API key as an environment variable)
# # genai.configure(api_key="AIzaSyDOf1kda2pOrMZsNwp7usXbb8g655UZ8GA")
# #
# # # Choose the model
# # model = genai.GenerativeModel('gemini-1.5-flash')
# #
# # # Global variable to store generated questions (for the session)
# # questions_list = []
# # current_score = 0
# #
# # # Function to generate multiple-choice questions
# # def generate_questions(topic):
# #     """Generates assessment questions for the given topic using Gemini Flash."""
# #     prompt = f"Generate 3 multiple-choice questions related to {topic}. " \
# #              "Provide 4 answer options for each question, with only one correct answer. " \
# #              "Format each question as follows:\n" \
# #              "Question: [Question text]\n" \
# #              "Options:\n" \
# #              "A) [Option 1]\n" \
# #              "B) [Option 2]\n" \
# #              "C) [Option 3]\n" \
# #              "D) [Option 4]\n" \
# #              "Correct Answer: [Letter of the correct answer (A, B, C, or D)]\n\n" \
# #             "After the correct answer, end with '$$'"
# #
# #     chat = model.start_chat(history=[])
# #     response = chat.send_message(prompt)
# #     print(response)
# #     questions = response.text.split("$$")
# #     print(questions)
# #     return questions
# #
# # # Function to parse a single question
# # # def parse_question(question_str):
# # #     """Parses the question and options from the given string."""
# # #     # Extract question using regular expression
# # #     question_match = re.search(r'\*\*Question:\*\* (.+)', question_str)
# # #     options_match = re.findall(r'([A-D])\) (.+)', question_str)
# # #     correct_answer_match = re.search(r'\*\*Correct Answer:\*\* ([A-D])', question_str)
# # #
# # #     question = question_match.group(1) if question_match else "Question not found"
# # #     options = {opt[0]: opt[1] for opt in options_match} if options_match else {}
# # #     correct_answer = correct_answer_match.group(1) if correct_answer_match else None
# # #     print("this is the questions",question)
# # #     print("these are the options",options)
# # #     print(correct_answer)
# # #     return question, options, correct_answer
# #
# # import re
# #
# #
# # def parse_question(question_str):
# #     """Parses a question string into question text, options, correct answer, and code block."""
# #     # Initialize variables
# #     question_text = ""
# #     options = {}
# #     correct_answer = ""
# #     code_block = ""
# #
# #     # Check if there's a code block
# #     if '```python' in question_str:
# #         code_block_match = re.search(r'```python(.*?)```', question_str, re.DOTALL)
# #         if code_block_match:
# #             code_block = code_block_match.group(1).strip()
# #             print("code block is \n",code_block)
# #             # Remove code block from question_str for further processing
# #             question_str = question_str.replace(code_block_match.group(0), '')
# #
# #     # Process remaining question text
# #     question_lines = question_str.split('\n')
# #     print("ques lines are\n",question_lines)
# #     for line in question_lines:
# #         line = line.strip()
# #         if line.startswith('**Question:**'):
# #             question_text = line.split(':**', 1)[1].strip()
# #         elif line.startswith('Options'):
# #             continue  # Skip 'Options' header line
# #         elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
# #             letter = line[0]
# #             option = line[2:].strip()
# #             options[letter] = option
# #         elif line.startswith('**Correct Answer'):
# #             correct_answer = line.split(':** ', 1)[1].strip()
# #     print("parsed",question_text, options, correct_answer)
# #     return question_text, options, correct_answer, code_block
# #
# #
# # # Function to assess answers using Gemini Flash
# # def assess_answer(topic, answer, question,code_block):
# #     """Assesses the student's answer using Gemini Flash."""
# #     prompt = f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n" \
# #              "Please provide a reason if the answer is correct or incorrect. keep is short and precise"
# #     chat = model.start_chat(history=[])
# #     response = chat.send_message(prompt)
# #     # Print response for debugging
# #     print("Assessment Response:", response.text)
# #     return response.text
# #
# # # Route for the home page
# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     global current_score
# #     current_score = 0  # Reset score when starting a new assessment
# #     if request.method == 'POST':
# #         topic = request.form.get('topic')
# #         return redirect(url_for('assessment', topic=topic))
# #     return render_template('home.html', score=current_score)
# #
# # # Route for the assessment
# # @app.route('/assessment/<topic>', methods=['GET', 'POST'])
# # def assessment(topic):
# #     global questions_list, current_score, code_block
# #
# #     if request.method == 'POST':
# #         selected_answer = request.form.get('answer')
# #         print(selected_answer)
# #         question = request.form.get('question')
# #
# #         # Assess the answer and get feedback
# #         feedback = assess_answer(topic, selected_answer, question,code_block)
# #         if "Correct" or "correct" in feedback:
# #             is_correct = "Correct Answer!"
# #             current_score += 1
# #         else:
# #             is_correct = None
# #         # Render the template with feedback and a Next button
# #         return render_template('home.html', topic=topic, question=None, options=None, score=current_score,
# #                                feedback=feedback, is_correct=is_correct)
# #
# #     # Handle the "Next" button to move to the next question
# #     if not questions_list:
# #         questions_list = generate_questions(topic)
# #
# #     if questions_list:
# #         next_question = questions_list.pop(0)
# #         print("next ques is\n",next_question)
# #         question_text, options, correct_answer, code_block = parse_question(next_question)
# #         return render_template('home.html', topic=topic, question=question_text, options=options, score=current_score,
# #                                feedback=None, is_correct=None, correct_answer=correct_answer, code_block=code_block)
# #     else:
# #         return render_template('home.html', topic=topic, question="Assessment Complete!", score=current_score,
# #                                feedback=None, is_correct=None)
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
# 
# from fastapi import FastAPI, HTTPException, APIRouter
# from pydantic import BaseModel
# import os
# import google.generativeai as genai
# import random
# import re
# from dotenv import load_dotenv
# import base64
# load_dotenv(".env")
# 
# app = FastAPI()
# router = APIRouter()
# 
# # Configure Google GenAI (Remember to set your API key as an environment variable)
# genai.configure(api_key=os.getenv("GENAI_API_KEY", os.getenv("GENAIAPI_KEY")))
# 
# # Choose the model
# model = genai.GenerativeModel('gemini-1.5-flash')
# 
# # Global variable to store generated questions (for the session)
# questions_list = []
# current_score = 0
# 
# # Data models
# class QuestionResponse(BaseModel):
#     question: str
#     options: dict
#     correct_answer: str
#     code_block: str = None
# 
# class AssessmentRequest(BaseModel):
#     topic: str
# 
# class SubmitAnswerRequest(BaseModel):
#     topic: str
#     selected_answer: str
#     question: str
#     code_block: str = None
# 
# class AssessmentResponse(BaseModel):
#     feedback: str
#     is_correct: bool
#     current_score: int
# 
# # Function to generate multiple-choice questions
# def generate_questions(topic: str):
#     """Generates assessment questions for the given topic using Gemini Flash."""
#     prompt = f"Generate 10 multiple-choice questions related to {topic}. " \
#              "Provide 4 answer options for each question, with only one correct answer. " \
#              "Format each question as follows:\n" \
#              "Question: [Question text]\n" \
#              "Options:\n" \
#              "A) [Option 1]\n" \
#              "B) [Option 2]\n" \
#              "C) [Option 3]\n" \
#              "D) [Option 4]\n" \
#              "Correct Answer: [Letter of the correct answer (A, B, C, or D)]\n\n" \
#              "After the correct answer, end with '$$'"
# 
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     questions = response.text.split("$$")
#     return questions
# 
# # Function to parse a single question
# def parse_question(question_str: str):
#     """Parses a question string into question text, options, correct answer, and code block."""
#     # Initialize variables
#     question_text = ""
#     options = {}
#     correct_answer = ""
#     code_block = ""
# 
#     # Check if there's a code block
#     if '```python' in question_str:
#         code_block_match = re.search(r'```python(.*?)```', question_str, re.DOTALL)
#         if code_block_match:
#             code_block = code_block_match.group(1).strip()
#             question_str = question_str.replace(code_block_match.group(0), '')
# 
#     # Process remaining question text
#     question_lines = question_str.split('\n')
#     for line in question_lines:
#         line = line.strip()
#         if line.startswith('**Question:**'):
#             question_text = line.split(':**', 1)[1].strip()
#         elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
#             letter = line[0]
#             option = line[2:].strip()
#             options[letter] = option
#         elif line.startswith('**Correct Answer'):
#             correct_answer = line.split(':** ', 1)[1].strip()
#     return question_text, options, correct_answer, code_block
# 
# # Function to assess answers using Gemini Flash
# def assess_answer(topic: str, answer: str, question: str, code_block: str):
#     """Assesses the student's answer using Gemini Flash."""
#     prompt = f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n" \
#              "Please provide a reason if the answer is correct or incorrect. keep it short and precise"
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     return response.text
# 
# # API endpoint to start a new assessment and generate questions
# @router.post("/start-assessment/")
# async def start_assessment(request: AssessmentRequest):
#     global questions_list, current_score
#     current_score = 0
#     questions_list = generate_questions(request.topic)
#     if not questions_list:
#         raise HTTPException(status_code=404, detail="No questions generated.")
#     return {"message": "Assessment started", "questions_available": len(questions_list)}
# 
# # API endpoint to get the next question
# @router.get("/next-question/", response_model=QuestionResponse)
# async def next_question():
#     global questions_list
#     if not questions_list:
#         raise HTTPException(status_code=404, detail="No more questions available.")
# 
#     next_question = questions_list.pop(0)
#     question_text, options, correct_answer, code_block = parse_question(next_question)
#     return {
#         "question": question_text,
#         "options": options,
#         "correct_answer": correct_answer,
#         "code_block": code_block
#     }
# 
# # API endpoint to submit an answer and get feedback
# @router.post("/submit-answer/", response_model=AssessmentResponse)
# async def submit_answer(request: SubmitAnswerRequest):
#     global current_score
#     feedback = assess_answer(request.topic, request.selected_answer, request.question, request.code_block)
#     is_correct = "Correct" in feedback or "correct" in feedback
#     if is_correct:
#         current_score += 1
#     return {
#         "feedback": feedback,
#         "is_correct": is_correct,
#         "current_score": current_score
#     }
# 
# 
# # To run the FastAPI app, use the following command:
# # uvicorn your_file_name:app --reload
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

    return questions


# Function to parse a single question
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
        if '```python' in question_str:
            code_block_match = re.search(r'```python(.*?)```', question_str, re.DOTALL)
            if code_block_match:
                code_block = code_block_match.group(1).strip()
                question_str = question_str.replace(code_block_match.group(0), '')

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

    return questions


# Function to assess answers using Gemini Flash
def assess_answer(question: str, answer: str, code_block: str):
    """Assesses the student's answer using Gemini Flash."""
    prompt = f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n" \
             "Please provide a reason if the answer is correct or incorrect. Keep it short and precise."
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text


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

    feedback = assess_answer(current_question['question'], request.selected_answer, request.code_block)
    is_correct = "Correct" in feedback or "correct" in feedback

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

    if not parsed_questions:
        raise HTTPException(status_code=500, detail="Failed to parse questions.")

    # Assume there is at least one question in parsed_questions
    question_data = parsed_questions[0]

    return question_data
