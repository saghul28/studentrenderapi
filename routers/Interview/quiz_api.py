from fastapi import FastAPI, HTTPException, Body ,status,APIRouter
from typing import List
from firebase_config import pyredb
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import random

router = APIRouter()

# Store the correct answers in a dictionary
correct_answers = {}

@router.get("/random_quizzes/{domain}")
async def get_random_quizzes(domain: str):
    quiz_ref = pyredb.child("quiz").child(domain)
    quiz_data = quiz_ref.get().val()
    quiz_list = list(quiz_data)
    
    if not quiz_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    quiz_indices = random.sample(range(len(quiz_list)), 10)
    quiz = []    
     
    for index in quiz_indices:
        question = quiz_list[index]["question"]
        options = quiz_list[index]["options"]
        number = quiz_list[index]["number"]
        answer = quiz_list[index]["answer"]
        quiz.append({"question":question,"options":options,"number":number})
        
        # Store the correct answer in the correct_answers dictionary
        correct_answers[number] = answer
        print(correct_answers)
    return {"quizzes": quiz}


class AnswerRequest(BaseModel):
   answers: List[str]

@router.post('/check_answer')
async def check_answer(answers: AnswerRequest = Body(...)):
    marks = sum(answer in correct_answers.values() for answer in answers.answers)
    
    # Convert dict_values object to list
    correct_answers_list = list(correct_answers.values())
    
    return JSONResponse(
        status_code=status.HTTP_200_OK, 
        content={"marks": marks, "correct_answer": correct_answers_list}
    )