from io import BytesIO
from fastapi import FastAPI, HTTPException, APIRouter, Depends, Query
from fastapi.responses import JSONResponse, StreamingResponse
import google.generativeai as genai
import random
from gtts import gTTS
from routers.account.user_api import get_api_key
from .asssesment import generate_questions, assess_answer, parse_question
from pydantic import BaseModel
import uuid

router = APIRouter()
genai.configure(api_key="AIzaSyBaJInUzY9hvQYVfr2TXUvY5UH7WmzjGsI")
model = genai.GenerativeModel('gemini-1.5-flash')

# In-memory session storage
user_sessions = {}

tech_topics = [
    "Artificial Intelligence", "Quantum Computing", "Cybersecurity", "Blockchain Technology",
    "Internet of Things (IoT)", "Cloud Computing", "5G Technology", "Augmented Reality (AR)",
    "Machine Learning", "Big Data Analytics"
]

class AnswerRequest(BaseModel):
    session_id: str
    answer: str

@router.post('/generate_questions')
async def api_generate_questions():
    """Generates questions and returns a session ID."""
    print(f"API Key: {get_api_key()}")
    
    topic = random.choice(tech_topics)
    questions = generate_questions(topic)
    if not questions:
        raise HTTPException(status_code=500, detail="Failed to generate questions")

    # Create a unique session ID
    session_id = str(uuid.uuid4())  # Generates a unique session ID

    # Store session data
    user_sessions[session_id] = {
        "topic": topic,
        "questions": questions,
        "current_index": 0,
        "score": 0
    }

    question_text, options, correct_answer, code_block = parse_question(questions[0])

    return JSONResponse(content={
        "message": "Questions generated successfully.",
        "session_id": session_id,
        "topic": topic,
        "first_question": {
            "question": question_text,
            "options": options,
            "code_block": code_block,
            "length": len(questions)
        }
    })

@router.get('/next_question')
async def api_next_question(session_id: str = Query(...)):
    """Fetches the next question using session ID."""
    session = user_sessions.get(session_id)
   
    if not session:
        raise HTTPException(status_code=400, detail="Invalid session.")

    if session["current_index"] >= len(session["questions"]) - 1:
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
    """Validates user's answer using session ID."""
    session = user_sessions.get(answer_request.session_id)
    if not session:
        raise HTTPException(status_code=400, detail="Invalid session.")

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

@router.api_route("/listen")
def voiceListen():
    """Generates a listening topic and returns an audio file."""
    topic = random.choice(tech_topics)
    prompt = f"Generate a simple and clear paragraph about {topic} for 300 words for a listening test."
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    paragraph = response.text.strip()

    tts = gTTS(paragraph)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)  # Move pointer to the beginning

    return StreamingResponse(audio_buffer, media_type="audio/mpeg", headers={"Content-Disposition": "inline; filename=speech.mp3"})
