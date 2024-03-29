from fastapi import APIRouter ,HTTPException, Query,status
from typing import List
import requests
from pydantic import BaseModel
from firebase_config import pyredb
from fastapi.responses import JSONResponse

router = APIRouter()


class StudentDetails(BaseModel):
    studentName : str
    studentCollege : str
    studentDepartment:str
    studentDegree:str
    studentProjectDomain:str
    studentEmail:str
    studentPhoneNumber:int
    


@router.post("/studentdetails")
async def studentDetails(request: StudentDetails):
    try:
        student_name = request.studentName
        student_college = request.studentCollege
        student_department = request.studentDepartment
        student_degree = request.studentDegree
        student_project_domain = request.studentProjectDomain
        student_email = request.studentEmail
        student_phone_number = request.studentPhoneNumber
       
        
        project_data = {
            'student_name': student_name,
            'student_college': student_college,
            'student_department': student_department,
            'student_degree': student_degree,
            'student_project_domain': student_project_domain,
            'student_email':student_email,
            'student_phone_number':student_phone_number
            
        }
        child_name = f"{student_name}_{student_college}"  
        
        pyredb.child('student').child(child_name).set(project_data)
        return JSONResponse(project_data, status_code=status.HTTP_201_CREATED)

    
    except Exception as e:
        return JSONResponse({"message": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


GITHUB_API_URL = "https://api.github.com/search/repositories"

def search_github(topic: str, language: str) -> List[dict]:
    
    params = {"q": f"{topic} language:{language}", "per_page": 5}  # You can adjust the number of results

    
    response = requests.get(GITHUB_API_URL, params=params)

    
    if response.status_code == 200:
        
        data = response.json()
        projects = []
        for item in data.get("items", []):
            project_info = {
                "title": item.get("name"),
                "description": item.get("description"),
                "url": item.get("html_url"),
                "project_domain": item.get("homepage") or ""
            }
            projects.append(project_info)
        return projects
    else:
     
        raise HTTPException(status_code=response.status_code, detail="GitHub API request failed")


@router.get("/search_projects/")
async def search_projects(
    topic: str,
    language: str = Query('en'),
):
    
    projects = search_github(topic, language)
    return {"projects": projects}




# class ProjectDetails(BaseModel):
#     title:str
#     description:str
#     degree:str
#     department:str
#     domain:str
    
# @router.post("/projectdetails")
# async def projectDetails(request: ProjectDetails):
#     try:
#         title = request.title
#         description = request.description
#         degree = request.degree
#         department = request.department
#         domain = request.domain
        
#         project_data = {
#             'title': title,
#             'description': description,
#             'degree': degree,
#             'department': department,
#             'domain': domain
#         }
#          # Corrected child name format
        
#         pyredb.child('projects').child(domain).child(title).set(project_data)
#         return JSONResponse(project_data, status_code=status.HTTP_201_CREATED)

#     except Exception as e:
        
#         raise HTTPException(status_code=503, detail="Service Unavailable")




# @router.get("/project-List")
# async def get_projects(domain: str = ''):
#     # Query Firebase to get details of projects in the specified department
#     get_details = pyredb.child("projects").child(domain).get()
    
#     # Initialize an empty list to store project details
#     project_details = []

#     # Extract project details from the response
#     try:
#         if get_details:
#             projects_data = get_details.val()
#             for project_data in projects_data.values():
#                 # Access the title and description for each project
#                 title = project_data.get('title', '')
#                 description = project_data.get('description', '')
#                 project_details.append({'title': title, 'description': description})

#             return project_details
#     except:
#         return JSONResponse("No projects found", status_code=status.HTTP_404_NOT_FOUND)
    
    