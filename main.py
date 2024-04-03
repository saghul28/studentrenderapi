from fastapi import FastAPI ,Depends,HTTPException,status
from routers.account import user_api
from routers.project import project_api
from routers.Interview import interview,quiz_api
from routers.course import course_api
from routers.Jobs import job_api
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
 
# Include your routers here
app.include_router( user_api.router, prefix="/user", tags=["user"])
app.include_router(project_api.router, prefix="/project", tags=["project"])
app.include_router(interview.router,prefix="/interview", tags=["interview"])
app.include_router(quiz_api.router,prefix="/interview", tags=["interview"])
app.include_router(course_api.router,prefix="/course", tags=["course"])
app.include_router(job_api.router,prefix="/job", tags=["job"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def hello(): 
    return {"messa ge":"hello world"}
