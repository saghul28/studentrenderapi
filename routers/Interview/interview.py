
from fastapi import APIRouter ,HTTPException, Response,status,Depends
from firebase_config import pyredb
from fastapi.responses import JSONResponse
from ..account.user_api import validate_token
router = APIRouter()


# def store_questions():
#     try:
#         domain = "sql"
#         html_ref = pyredb.child("questions").child(domain)  # Creating a reference to the "html" category
#         questions = []  # List to store all HTML questions
#         for question in sql_questions:
#             questions.append({  # Append each question to the list
#                 'number':question['number'],
#                 'question': question['question'],
#                 'answer': question['answer'],
#                 'learned':False
                
#             })
#         html_ref.set(questions)  # Set the list of HTML questions under the "html" category
#         print("HTML questions stored successfully.")
#     except Exception as e:
#         print(e)

# def store_quiz():
#     try:
#         domain = "sql"
#         quiz_store = pyredb.child("quiz").child(domain)
#         quiz_questions = []

#         for quiz in sql_quiz:
#             question_data = {
#                 'number': quiz['number'],
#                 'question': quiz['question'],
#                 'options': quiz['options'],  # Use the 'options' list directly
#                 'answer': quiz['answer'],
#                 'isCorrect':False
#             }

#             quiz_questions.append(question_data)

#         quiz_store.set(quiz_questions)
#         print("SQL quiz stored successfully.")
#     except Exception as e:
#         print("Exception: " + str(e))


# # store_questions()
# store_quiz()


# @router.get("/question")
# async def get_question(domain: str = ''):
#
#     get_details = pyredb.child("questions").child(domain).get()
#     question_data = get_details.val()
#     project_details = []
#
#
#     try:
#         if question_data:
#
#             for project_data in question_data:
#                 # Access the title and description for each project
#                 number= project_data.get('number','')
#                 question = project_data.get('question', '')
#                 answer = project_data.get('answer', '')
#                 project_details.append({'number':number,'question': question, 'answer': answer})
#
#             return JSONResponse({ "data":project_details }, status_code=status.HTTP_200_OK)
#     except:
#         return JSONResponse("No projects found", status_code=status.HTTP_404_NOT_FOUND)
#
#
# @router.get('/quiz')
# async def get_quiz(domain: str ,current_user: str = Depends(validate_token)):
#
#     get_details = pyredb.child("quiz").child(domain).get()
#     quiz_data = get_details.val()
#
#
#     quiz_details = []
#
#
#     try:
#         if quiz_data:
#
#             for project_data in quiz_data:
#
#                 number= project_data.get('number','')
#                 question = project_data.get('question', '')
#                 answer = project_data.get('answer', '')
#                 options = project_data.get('options',[])
#                 quiz_details.append({'number':number,'question': question,'options':options ,'answer': answer})
#
#             return quiz_details
#     except:
#         return JSONResponse("No projects found", status_code=status.HTTP_404_NOT_FOUND)
#
    
    