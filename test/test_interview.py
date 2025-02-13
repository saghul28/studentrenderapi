import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure the test folder can access the main app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app  # Import FastAPI app

client = TestClient(app)

def test_generate_questions():
    """Test generating questions and retrieving session ID."""
    response = client.post("/interview/generate_questions", json={"topic": "Python"})
    assert response.status_code == 200
    data = response.json()
    
    print("Generated Response:", data)  # Debugging
    
    assert "session_id" in data  # Ensure session ID is returned
    return data["session_id"]

def test_next_question():
    """Test fetching the next question."""
    session_id = test_generate_questions()  # Get a session ID
    print("Session ID:", session_id)  # Debugging
    
    response = client.get(f"/interview/next_question/{session_id}")
    
    print("Next Question Response:", response.json())  # Debugging
    assert response.status_code == 200

def test_submit_answer():
    """Test submitting an answer."""
    session_id = test_generate_questions()  # Get a session ID
    print("Session ID for Submit Answer:", session_id)  # Debugging
    
    response = client.post("/interview/submit_answer", json={"session_id": session_id, "answer": "A"})
    
    print("Submit Answer Response:", response.json())  # Debugging
    assert response.status_code == 200