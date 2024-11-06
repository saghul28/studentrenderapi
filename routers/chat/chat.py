from fastapi import  Form,APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import os

client = genai.configure(api_key=os.getenv("GENAIAPI_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
router = APIRouter()

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

    chat = model.start_chat(history=[],system_prompt=system_prompt)
    response = chat.send_message(prompt)
    
    return response.text
    
   


@router.post("/chat/ss")
async def chat(message: str = Form(default="How To learn Coding"), language: str = Form(...)):
    # Get the GPT response based on the user's input and selected language
    response = get_gpt_response(message, language)
    return {"response": response}


@router.post("/chat")
async def chat(request:ChatRequest):
    # Get the GPT response based on the user's input and selected language
    response = get_gpt_response(request.message, request.language)
    return {"response": response}





