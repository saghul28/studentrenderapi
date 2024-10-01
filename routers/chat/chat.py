from fastapi import FastAPI, Form,APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

router = APIRouter()
# Request model
class ChatRequest(BaseModel):
    message: str
    language: str


def get_gpt_response(prompt: str, language: str):
   
    if language == "english":
        system_prompt = "You are a helpful assistant that responds in English."
    elif language == "tamil":
        system_prompt = (
            "You are a helpful assistant that responds in Tamil, but don't translate English-origin words like names, nouns, or common words. "
            "If the word is English, keep it in English."
        )
    elif language == "tanglish":
        system_prompt = (
            "You are a helpful assistant that responds in colloquial Tamil but using English letters. Don't use Tamil script."
        )


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


# @router.post("/chat")
# async def chat(message: str = Form(default="How To learn Coding"), language: str = Form(...)):
#     # Get the GPT response based on the user's input and selected language
#     response = get_gpt_response(message, language)
#     return {"response": response}


@router.post("/chat")
async def chat(request:ChatRequest):
    # Get the GPT response based on the user's input and selected language
    response = get_gpt_response(request.message, request.language)
    return {"response": response}





