
# from fastapi import FastAPI ,Depends,HTTPException,status
# from routers.account import user_api
# from routers.project import project_api
# from routers.Interview import interview,quiz_api
# from routers.course import course_api
# from routers.Jobs import job_api
# from routers.Blog import blog
# from routers.Interview import asssesment
# from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import SessionMiddleware, Session
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

from routers.Blog import blog
from routers.Interview import asssesment
from routers.Jobs import job_api
from routers.Report import reportgen
# from routers.Report import 
from routers.account import user_api
from routers.course import course_api
from routers.project import project_api
from routers.chat import chat



app = FastAPI()




app.include_router( user_api.router, prefix="/user", tags=["User"])
app.include_router(project_api.router, prefix="/project", tags=["Project"])
# app.include_router(interview.router,prefix="/interview", tags=["interview"])
# app.include_router(quiz_api.router,prefix="/interview", tags=["interview"])
app.include_router(asssesment.router,prefix="/interview", tags=["Chatgpt"])
app.include_router(course_api.router,prefix="/course", tags=["Course"])
app.include_router(job_api.router,prefix="/job", tags=["Job"])
app.include_router(blog.router,prefix="/blog", tags=["Blog"])
app.include_router(reportgen.router,prefix="/report", tags=["Reports"])
app.include_router(chat.router,prefix="/chat", tags=["Chat"])

# app.include_router(abs)


app.add_middleware(SessionMiddleware , secret_key="your_secret_key")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def hello(): 
    return {"message":"hello world"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
