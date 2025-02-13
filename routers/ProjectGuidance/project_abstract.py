from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from docx import Document
from fastapi.responses import FileResponse,StreamingResponse
import io
import google.generativeai as generativeAI
from google.generativeai import types
from google import genai
from PIL import Image
from io import BytesIO
from pptx import  Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os
from dotenv import load_dotenv
from routers.account.user_api import get_api_key



def mygemai(prompt):
    try:
        # Configure genai with the API key
        client = generativeAI.configure(api_key=get_api_key())
        # Create the model instance and start the chat
        model = generativeAI.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text.replace("#", "").replace("*", "")

    except Exception as e:
        # Check if the error is related to the API key
        if "invalid API key" in str(e).lower():
            return "Error: Invalid API key. Please check your API key."
        return f"Error in generating content: {str(e)}"

# client = genai.Client(api_key=get_api_key())

router = APIRouter() 

class StudentProjectDetails(BaseModel):
    projectName:str
    degree:str
    department:str
    projectDescription:str
    frontend:str
    backend:str
    

@router.post('/abstract')
async def generatingAbstrct(studentDetails: StudentProjectDetails):
    prompt = (
        f"Create a comprehensive and detailed project abstract for a {studentDetails.degree} degree in {studentDetails.department}. "
        f"The project is titled '{studentDetails.projectName}', and its goal is to {studentDetails.projectDescription}. The abstract should be "
        f"divided into clearly defined sections, with a minimum of three pages of content. Each section should be "
        f"thorough and elaborate to ensure a deep understanding of the project.\n\n"
        f"1. **Introduction**:\n"
        f"   - Start with an introduction to the project, including the problem being solved and its relevance to the field. "
        f"   - Provide background information about the problem, its significance, and the motivation behind this project. "
        f"   - Mention why this project is important, its potential impact, and its scope.\n\n"
        f"2. **Project Details**:\n"
        f"   - Describe the overall objectives and goals of the project. "
        f"   - Provide a detailed breakdown of the methodologies used and the expected outcomes. "
        f"   - Explain how this project is innovative or unique compared to similar projects. "
        f"   - Include the key technologies involved in the project and how they contribute to achieving the project goals.\n\n"
        f"3. **Frontend**:\n"
        f"   - Describe the {studentDetails.frontend} technologies used, such as frameworks and libraries. "
        f"   - Explain why these technologies were chosen for the project. "
        f"   - Discuss how the {studentDetails.frontend} provides a user-friendly experience and supports the project's objectives. "
        f"   - Highlight key features like responsiveness, interactivity, or accessibility.\n\n"
        f"4. **Backend**:\n"
        f"   - Detail the backend technologies used, including frameworks, databases, and server-side technologies. "
        f"   - Discuss the reasons for choosing these technologies, focusing on scalability, performance, and security. "
        f"   - Explain how the {studentDetails.backend} handles data processing, storage, and integration with the {studentDetails.frontend}.\n\n"
        f"5. **System Recommendations**:\n"
        f"   - Provide suggestions for improving the system in the future, such as enhancing performance, adding new features, "
        f"     or improving security. "
        f"   - Recommend strategies for scaling the project as usage increases, ensuring sustainability and reliability. "
        f"   - Discuss potential areas for further research or development, including emerging technologies that could improve the system.\n\n"
        f"Ensure that the abstract is structured, technical, and written in a professional tone. "
        f"Make sure each section is detailed enough to fill at least one full page, focusing on providing a deep understanding "
        f"of the project’s goals, technologies, and future directions."
    )
    final_response = mygemai(prompt)
    print(final_response)

    if final_response.startswith("Error in generating content"):
        raise HTTPException(status_code=400, detail="Please login With Your Username and Password")

    doc = Document()
    doc.add_heading(f'Project Abstract: {studentDetails.projectName}', level=0)
    doc.add_paragraph(final_response)

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
  
    return StreamingResponse(
        file_stream,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f"attachment; filename=project_abstract_{studentDetails.projectName}.docx"
        },
    )

@router.post("/generate_projects_steps")
def generateSteps(studentDetails:StudentProjectDetails):
    prompt = (
    f"Create a detailed, step-by-step guide for a project titled '{studentDetails.projectName}', designed for a {studentDetails.degree} degree in {studentDetails.department}. "
    f"The goal of the project is to {studentDetails.projectDescription}. The guide should be divided into clearly defined sections, with each step providing a detailed explanation of the process, technologies used, code structure, and challenges faced. "
    f"The final document should be comprehensive, technical, and cover at least five pages.\n\n"

    f"1. **Introduction**:\n"
    f"   - Provide a brief overview of the project, its objectives, and the technologies that will be used. \n"
    f"   - Describe the project scope and explain its relevance to the field of {studentDetails.department}.\n"
    f"   - Define the importance of each phase of the project.\n\n"

    f"2. **Planning Stage**:\n"
    f"   - Detail the initial planning and research phase. Discuss how the requirements for the project were gathered.\n"
    f"   - Explain how the project objectives were established and refined.\n"
    f"   - Include information on the timeline, resources needed, and the initial feasibility study.\n"
    f"   - Software Declaration: Include the tools and platforms used for project management (e.g., Trello, Jira, etc.).\n\n"

    f"3. **Design Stage**:\n"
    f"   - Discuss the design phase in detail. Explain the system architecture, user interface, and user experience design.\n"
    f"   - Describe how the frontend and backend components were planned, including wireframes, database schemas, and system workflows.\n"
    f"   - Provide the **initial folder structure** for the project. For example, describe the directories for the frontend, backend, and database scripts.\n"
    f"     Example folder structure:\n"
    f"     - /frontend: Contains all frontend-related code (React components, stylesheets, etc.)\n"
    f"     - /backend: Contains all backend-related code (API routes, models, controllers, etc.)\n"
    f"     - /database: Contains scripts for database schema and migrations\n"
    f"   - Software Declaration: List the design tools used, such as Figma, Adobe XD, or similar tools.\n\n"

    f"4. **Development Stage**:\n"
    f"   - Break down the development phase into smaller steps, describing how each component of the system (frontend, backend, database) was developed.\n"
    f"   - **Database Structure**: Provide a clear description of the database schema, including tables, relationships, and any indexes used. For example, describe how users are stored in a 'users' table with fields for user ID, name, email, and password.\n"
    f"     Example database structure:\n"
    f"     - **Users table**: user_id (Primary Key), name, email, password\n"
    f"     - **Projects table**: project_id (Primary Key), user_id (Foreign Key), project_name, description\n"
    f"   - Provide examples of **initial code** that needs to be written. For example, creating a basic API with FastAPI, including a route for user registration, and integrating it with the database.\n"
    f"   - Provide an overview of the development process for both the frontend and backend, explaining how technologies like {studentDetails.frontend} (e.g., React, Vue.js, Angular) and {studentDetails.backend} (e.g., Flask, FastAPI, Django) were integrated.\n"
    f"   - Discuss key features such as authentication, data processing, and any major challenges encountered during the development phase.\n"
    f"   - Software Declaration: Clearly mention all programming languages, frameworks, libraries, and tools used in development. For example:\n"
    f"     - Frontend: {studentDetails.frontend}\n"
    f"     - Backend: {studentDetails.backend}\n"
    f"     - Database: MySQL/PostgreSQL\n"
    f"     - Other Tools: Git, Docker, etc.\n\n"

    f"5. **Testing and Quality Assurance**:\n"
    f"   - Describe the testing process in detail, including unit tests, integration tests, and user acceptance tests.\n"
    f"   - Discuss how the system was evaluated for scalability, performance, and security.\n"
    f"   - Mention any tools or libraries used for testing and debugging.\n"
    f"   - Software Declaration: Include tools like Postman for API testing, Selenium for UI testing, or Jest for unit testing.\n\n"

    f"6. **Deployment Stage**:\n"
    f"   - Explain the deployment process, including how the application was deployed to production.\n"
    f"   - Describe the steps taken for setting up servers, configuring cloud services, and ensuring continuous deployment.\n"
    f"   - Highlight any configuration management tools or scripts used for automation.\n"
    f"   - Software Declaration: Mention the deployment platforms or tools used, such as AWS, Heroku, Docker, or Kubernetes.\n\n"

    f"7. **Maintenance and Updates**:\n"
    f"   - Provide a plan for ongoing maintenance, bug fixes, and feature updates after the project has been deployed.\n"
    f"   - Explain how the system will be monitored for performance and errors, and how updates will be rolled out.\n"
    f"   - Discuss the role of version control (e.g., Git) in managing code updates.\n\n"

    f"8. **Conclusion**:\n"
    f"   - Summarize the project steps and how each phase contributed to achieving the project’s goals.\n"
    f"   - Discuss the lessons learned during the process and potential improvements for future iterations.\n"
    f"   - Provide recommendations for further development or research.\n\n"

    f"Ensure that each section is detailed enough to provide a full understanding of the project’s process, including the technologies, code structure, folder structure, and tools used at each stage. Focus on delivering a well-structured and technical document that can span at least five pages.\n\n"

    f"The result should be a step-by-step guide that not only outlines the phases of the project but also provides clarity on the technologies, code setup, and tools used at each stage of development."
    )

    final_response = mygemai(prompt)
    doc = Document()
    doc.add_heading(f'Project Steps:{studentDetails.projectName}',0)
    doc.add_paragraph(final_response.replace("#","").replace("*",""))
    
    file_path = f"project_Steps_{studentDetails.projectName}.docx"
    doc.save(file_path)
    return FileResponse(file_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename=file_path)


# 
@router.post("/generate_report")
def project_report(studentDetails: StudentProjectDetails):
    prompts = [
        # Prompt 1: Introduction
        f"Generate the **Introduction** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Project Background\n"
        f"2. Problem Statement\n"
        f"3. Objectives\n"
        f"4. Technologies Overview ({studentDetails.frontend}, {studentDetails.backend}, PostgreSQL)\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 2: Project Planning and Requirements
        f"Generate the **Project Planning and Requirements** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Project Scope and Requirements\n"
        f"2. Technology Stack Selection (Why {studentDetails.frontend}, {studentDetails.backend})\n"
        f"3. User Stories/Use Cases\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 3: System Design and Architecture
        f"Generate the **System Design and Architecture** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. High-Level System Architecture ({studentDetails.frontend}/{studentDetails.backend} interaction, API design)\n"
        f"2. Database Design (PostgreSQL schema for inventory tracking)\n"
        f"3. API Design ({studentDetails.backend} endpoints, RESTful routes)\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 4: Frontend Development
        f"Generate the **Frontend Development** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. {studentDetails.frontend} Overview\n"
        f"2. State Management in {studentDetails.frontend}\n"
        f"3. User Interface Design and Responsiveness\n"
        f"4. Code Snippets for Frontend Features\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 5: Backend Development
        f"Generate the **Backend Development** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. {studentDetails.backend} Overview\n"
        f"2. Database Interaction\n"
        f"3. API Design and Security (JWT Authentication, API Routes)\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 6: Testing and Quality Assurance
        f"Generate the **Testing and Quality Assurance** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Testing Strategy (Unit, Integration Testing) in {studentDetails.frontend} and {studentDetails.backend}\n"
        f"2. Tools Used\n"
        f"3. Code Coverage and Bug Fixes\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 7: Deployment
        f"Generate the **Deployment** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Deployment Platform (Heroku, AWS EC2, or Docker)\n"
        f"2. CI/CD Pipeline (GitHub Actions, Docker)\n"
        f"3. Steps for Deployment\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 8: Challenges and Solutions
        f"Generate the **Challenges and Solutions** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Key Challenges (e.g., managing database consistency, API performance)\n"
        f"2. Solutions Implemented (e.g., database indexing, caching)\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 9: Conclusion
        f"Generate the **Conclusion** section for the project titled '{studentDetails.projectName}'. "
        f"Include the following subtopics:\n"
        f"1. Project Summary\n"
        f"2. Lessons Learned\n"
        f"3. Future Improvements (e.g., adding more features, scaling for larger enterprises)\n\n"
        f"Write 300-400 words for this section.",

        # Prompt 10: Index
        f"Generate the **Index** for the project titled '{studentDetails.projectName}'. "
        f"The index should list all the sections and subtopics in the report:\n"
        f"1. Introduction\n"
        f"2. Project Planning and Requirements\n"
        f"3. System Design and Architecture\n"
        f"4. Frontend Development\n"
        f"5. Backend Development\n"
        f"6. Testing and Quality Assurance\n"
        f"7. Deployment\n"
        f"8. Challenges and Solutions\n"
        f"9. Conclusion\n\n"
        f"Ensure the index is concise and fits on the first page."
    ]

    # Generate responses for each prompt
    responses = []
    for prompt in prompts:
        response = mygemai(prompt)
        responses.append(response)

    # Create a Word document
    doc = Document()
    doc.add_heading(f'Project Report: {studentDetails.projectName}', 0)

    # Add the index
    doc.add_heading('Index', level=1)
    doc.add_paragraph(responses[-1])

    # Add the remaining sections
    section_titles = [
        "Introduction",
        "Project Planning and Requirements",
        "System Design and Architecture",
        "Frontend Development",
        "Backend Development",
        "Testing and Quality Assurance",
        "Deployment",
        "Challenges and Solutions",
        "Conclusion"
    ]

    for i, title in enumerate(section_titles):
        doc.add_heading(title, level=1)
        doc.add_paragraph(responses[i].replace("#", "").replace("*", ""))

    # Save the document
    file_path = f"project_report_{studentDetails.projectName}.docx"
    doc.save(file_path)

    # Return the document as a response
    return FileResponse(
        file_path,
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        filename=file_path
    )
    
    
@router.post("/generate-ppt/")
async def generate_ppt(details: StudentProjectDetails):
    """Generates a PowerPoint presentation with AI content, ensuring content overflow moves to a new slide."""
    ppt_file = f"{details.projectName.replace(' ', '_')}.pptx"
    prs = Presentation()

    # Slide 1: Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = details.projectName
    slide.placeholders[1].text = f"{details.degree}, {details.department}"

    # Sections to be generated dynamically
    section_titles = [
        "Project Overview", "Technologies Used", "System Architecture",
        "Key Features", "Additional Features", "Use Cases",
        "Future Scope", "Conclusion"
    ]

    # Generate AI content for each section
    sections = {}
    for title in section_titles:
        prompt = f"Generate 2-3 key topics under '{title}' for a {details.projectName} project, each with 3-4 bullet points."
        sections[title] = mygemai(prompt)

    # Function to add slides while ensuring content fits
    def add_slide_with_text(title, content_lines):
        """Adds content to slides, moving overflow text to new slides."""
        MAX_LINES_PER_SLIDE = 5  # Limit to prevent overcrowding
        slide_number = 1  # Track slide number for the same section
        FONT_SIZE = Pt(18)  # Reduced font size (default is usually 18 or 20)

        while content_lines:
            slide = prs.slides.add_slide(prs.slide_layouts[1])
            slide.shapes.title.text = f"{title} (Part {slide_number})" if slide_number > 1 else title
            text_box = slide.placeholders[1]
            text_frame = text_box.text_frame
            text_box.top = Inches(1.5) 
            text_frame.clear()

            # Add content lines to the slide
            for _ in range(min(MAX_LINES_PER_SLIDE, len(content_lines))):
                para = text_frame.add_paragraph()
                para.text = f"• {content_lines.pop(0)}"
                
                para.space_after = Inches(0.2)
                # Set font size for the paragraph
                for run in para.runs:
                    run.font.size = FONT_SIZE

            slide_number += 1  # Increment slide number for the next part

    # Generate slides dynamically
    for section, content in sections.items():
        content_lines = [line.strip() for line in content.split("\n") if line.strip()]
        add_slide_with_text(section, content_lines)

    # Save and Return the File
    prs.save(ppt_file)
    return FileResponse(ppt_file, filename=ppt_file, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")#     Generate an image using Google Generative AI.
#     """
#     try:
#         response = client.models.generate_images(
#             model='imagen-3.0-generate-002',
#             prompt=prompt,
#             config=types.GenerateImagesConfig(
#                 number_of_images=1,
#             )
#         )
#         if response.generated_images:
#             image_bytes = response.generated_images[0].image.image_bytes
#             return Image.open(BytesIO(image_bytes))
#         return None
#     except Exception as e:
#         print(f"Error generating image: {e}")
#         return None
