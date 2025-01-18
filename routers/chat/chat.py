from fastapi import Form, APIRouter, HTTPException, Response
from pydantic import BaseModel
import google.generativeai as genai
import os
from routers.account.user_api import get_api_key

router = APIRouter()

# Initialize the router, without calling genai.client until after login.
  # Initially set client to None, to be initialized later.
global client

# Define ChatRequest for input
class ChatRequest(BaseModel):
    message: str
    language: str


# Function to initialize client with API key if available
def initialize_client():

    api_key = get_api_key()  # Get API key from global storage (ensure it's set)
    if api_key is None:
        raise HTTPException(status_code=400, detail="API key is not set")

    client = genai.configure(api_key=api_key)  # Initialize the client with the API key
    return client


# Function to generate GPT response
def get_gpt_response(prompt: str, language: str, client=None):

    if client is None:
        initialize_client()

    # Language-specific prompts
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

    # Send the message to the GPT model and get the response
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)

    return response.text


# Endpoint to handle chat using Form data
@router.post("/chat/ss")
async def chat(message: str = Form(default="How To learn Coding"), language: str = Form(...)):
    # Get the GPT response based on the user's input and selected language
    response = get_gpt_response(message, language)
    return {"response": response}


# Endpoint to handle chat using Pydantic model
@router.post("/chat")
async def chat(request: ChatRequest):
    api_key = get_api_key()
    print(api_key)
    # Get the GPT response based on the user's input and selected language
    response = get_gpt_response(request.message, request.language)
    return {"response": response}

