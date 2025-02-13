# import base64
# from io import BytesIO
# from fastapi import FastAPI, HTTPException, APIRouter
# from fastapi.responses import JSONResponse, StreamingResponse
# from pydantic import BaseModel
# import os
# import google.generativeai as genai
# import re
# import random
# from gtts import gTTS
# from routers.account.user_api import get_api_key


# router = APIRouter()

# # genai.configure(api_key=get_api_key())
# genai.configure(api_key="AIzaSyBaJInUzY9hvQYVfr2TXUvY5UH7WmzjGsI")
# model = genai.GenerativeModel('gemini-1.5-flash')

# questions_list = {}
# current_score = 0
# current_question_index = {}
# current_topic = ""

# class QuestionRequest(BaseModel):
#     topic: str

# class AnswerRequest(BaseModel):
#     answer: str

# def generate_questions(topic):
#     """Generates assessment questions for the given topic using Gemini Flash."""
#     prompt = (f"Generate 10 multiple-choice questions related to {topic}. "
#               "Provide 4 answer options for each question, with only one correct answer. "
#               "Format each question as follows:\n"
#               "Question: [Question text]\n"
#               "Options:\n"
#               "A) [Option 1]\n"
#               "B) [Option 2]\n"
#               "C) [Option 3]\n"
#               "D) [Option 4]\n"
#               "Correct Answer: [Letter of the correct answer (A, B, C, or D)]\n\n"
#               "After the correct answer, end with '$$'")

#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     questions = response.text.split("$$")
   
#     return [q.strip() for q in questions if q.strip()]  

# def parse_question(question_str):
#     """Parses a question string into question text, options, correct answer, and code block."""
#     question_text = ""
#     options = {}
#     correct_answer = ""
#     code_block = ""

#     print(question_str)
#     if any(mark in question_str for mark in ['```', '``', '`']):
#         code_block_match = re.search(r'```[a-zA-Z]*\n(.*?)```', question_str, re.DOTALL)
#         print(code_block_match)
#         if code_block_match:
#             code_block = code_block_match.group(1).strip()
#             question_str = question_str.replace(code_block_match.group(0), '')

   
#     question_lines = question_str.split('\n')
#     for line in question_lines:
#         line = line.strip()
#         print("Line",line)
#         if line.startswith(('**Question:', 'Question')):
#             question_text = line.split(":",1)[1].strip()
#             print("QuestionText",question_text)
#         elif line.startswith('Options'):
#             continue  
#         elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
#             letter = line[0]
#             option = line[2:].strip()
#             options[letter] = option
#         elif line.startswith('Correct Answer:'):
#             correct_answer = line.split(':', 1)[1].strip()

#     return question_text, options, correct_answer, code_block


# def assess_answer(answer, question, code_block):
#     """Assesses the student's answer using Gemini Flash."""
#     if not question:
#         return "Error: Question context is missing."

#     prompt = (f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n"
#               "Please provide a reason if the answer is correct and if the answer is  incorrect provide the correct answer and reason. Keep it short and precise.")
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     return response.text

# @router.post('/generate_questions')
# async def api_generate_questions(request: QuestionRequest):
#     print(f"get api key i questions{get_api_key()}")
#     global questions_list, current_score, current_question_index, current_topic
#     current_score = 0  
#     topic = request.topic

#     if not topic:
#         raise HTTPException(status_code=400, detail="Topic is required")

#     questions = generate_questions(topic)
#     if not questions:
#         raise HTTPException(status_code=500, detail="Failed to generate questions")

#     questions_list[topic] = questions
#     current_question_index[topic] = 0  
#     current_topic = topic
#     question_text, options, correct_answer, code_block = parse_question(questions_list[topic][0])
    
#     return JSONResponse(content={
#         "message": "Questions generated successfully.",
#         "topic": topic,
#         "first_question": {
#             "question": question_text,
#             "options": options,
#             "code_block": code_block,
#             "length":len(questions_list[topic])
            
#         }
#     })

# # Endpoint to get the next question
# @router.get('/next_question')
# async def api_next_question():
#     global questions_list, current_question_index, current_topic

#     topic = current_topic
#     if not topic or topic not in questions_list or current_question_index.get(topic) is None:
#         raise HTTPException(status_code=400, detail="No questions available for the topic or generate questions first.")

#     if current_question_index[topic] >= len(questions_list[topic]):
#         return JSONResponse(content={"message": "No more questions available."})

    
#     current_question_index[topic] +=1
#     question_text, options, correct_answer, code_block = parse_question(questions_list[topic][current_question_index[topic]])
    
#     return JSONResponse(content={
#         "question": question_text,
#         "options": options,
#         "code_block": code_block
#     })


# @router.post('/submit_answer')
# async def api_submit_answer(answer_request: AnswerRequest):
#     global current_score, current_topic, current_question_index

#     answer = answer_request.answer

#     if not answer:
#         raise HTTPException(status_code=400, detail="Answer is required")

#     topic = current_topic

#     if not topic or topic not in questions_list or current_question_index.get(topic) is None:
#         raise HTTPException(status_code=400, detail="No questions generated for the topic.")

#     question_index = current_question_index[topic] 
#     if question_index < 0:
#         raise HTTPException(status_code=400, detail="No previous question to assess.")

#     # Assess the previous question's answer
#     question_text, options, correct_answer, code_block = parse_question(questions_list[topic][question_index])
#     feedback = assess_answer(answer, question_text, code_block)

#     is_correct = "incorrect" not in feedback.lower()
#     if is_correct:
#         current_score += 1

#     return JSONResponse(content={
#         "feedback": feedback,
#         "is_correct": is_correct,
#         "current_score": current_score
#     })


from fastapi import FastAPI, HTTPException, APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import google.generativeai as genai
import re
import uuid

router = APIRouter()

genai.configure(api_key="AIzaSyBaJInUzY9hvQYVfr2TXUvY5UH7WmzjGsI")
model = genai.GenerativeModel('gemini-1.5-flash')

# Store user sessions
user_sessions = {}

class QuestionRequest(BaseModel):
    topic: str

class AnswerRequest(BaseModel):
    session_id: str
    answer: str

def generate_questions(topic):
    """Generates assessment questions for the given topic using Gemini Flash."""
    prompt = (f"Generate 10 multiple-choice questions related to {topic}. "
              "Provide 4 answer options for each question, with only one correct answer. "
              "Format each question as follows:\n"
              "Question: [Question text]\n"
              "Options:\n"
              "A) [Option 1]\n"
              "B) [Option 2]\n"
              "C) [Option 3]\n"
              "D) [Option 4]\n"
              "Correct Answer: [Letter of the correct answer (A, B, C, or D)]\n\n"
              "After the correct answer, end with '$$'")

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    questions = response.text.split("$$")
   
    return [q.strip() for q in questions if q.strip()]  

def parse_question(question_str):
    """Parses a question string into question text, options, and correct answer."""
    question_text = ""
    options = {}
    correct_answer = ""
    code_block = ""

    question_lines = question_str.split('\n')
    for line in question_lines:
        line = line.strip()
        if line.startswith(('**Question:', 'Question')):  
            question_text = line.split(":",1)[1].strip()
        elif line.startswith('A)') or line.startswith('B)') or line.startswith('C)') or line.startswith('D)'):
            letter = line[0]
            option = line[2:].strip()
            options[letter] = option
        elif line.startswith('Correct Answer:'):
            correct_answer = line.split(':', 1)[1].strip()

    return question_text, options, correct_answer, code_block

def assess_answer(answer, question, code_block):
    """Assesses the student's answer using Gemini Flash."""
    if not question:
        return "Error: Question context is missing."

    prompt = (f"Is the following answer correct for the question \"{question}{code_block}\":\n\n{answer}\n\n"
              "Please provide a reason if the answer is correct and if the answer is  incorrect provide the correct answer and reason. Keep it short and precise.")
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text

@router.post('/generate_questions')
async def api_generate_questions(request: QuestionRequest):
    """Generates questions for a specific topic and assigns a session."""
    session_id = str(uuid.uuid4())  # Generate unique session ID

    questions = generate_questions(request.topic)
    if not questions:
        raise HTTPException(status_code=500, detail="Failed to generate questions")

    user_sessions[session_id] = {
        "topic": request.topic,
        "questions": questions,
        "current_index": 0,
        "score": 0
    }

    question_text, options, correct_answer, code_block = parse_question(questions[0])

    return JSONResponse(content={
        "message": "Questions generated successfully.",
        "session_id": session_id,
        "topic": request.topic,
        "first_question": {
            "question": question_text,
            "options": options,
            "code_block": code_block,
            "length": len(questions)
        }
    })


@router.get('/next_question')
async def api_next_question(session_id: str = Query(...)):
    """Fetches the next question for a given session."""
    
    if session_id not in user_sessions:
        raise HTTPException(status_code=400, detail="Invalid session ID.")

    session = user_sessions[session_id]
    
    if session["current_index"] >= len(session["questions"]):
        return JSONResponse(content={"message": "No more questions available."})

    session["current_index"] += 1
    question_text, options, correct_answer, code_block = parse_question(session["questions"][session["current_index"]])

    return JSONResponse(content={
        "question": question_text,
        "options": options,
        "code_block": code_block
    })


@router.post('/submit_answer')
async def api_submit_answer(answer_request: AnswerRequest):
    """Validates user's answer and updates the score."""
    session_id = answer_request.session_id
    if session_id not in user_sessions:
        raise HTTPException(status_code=400, detail="Invalid session ID.")

    session = user_sessions[session_id]
    current_index = session["current_index"]

    if current_index < 0 or current_index >= len(session["questions"]):
        raise HTTPException(status_code=400, detail="No question to assess.")

    question_text, options, correct_answer, code_block = parse_question(session["questions"][current_index])
    
    feedback = assess_answer(answer_request.answer, question_text, code_block)
    is_correct = "incorrect" not in feedback.lower()

    if is_correct:
        session["score"] += 1

    return JSONResponse(content={
        "feedback": feedback,
        "is_correct": is_correct,
        "current_score": session["score"]
    })
