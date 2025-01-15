from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from routers.Blog import blog
from routers.Interview import asssesment
from routers.Jobs import job_api
from routers.Report import reportgen
from routers.account import user_api
from routers.course import course_api
from routers.project import project_api
from routers.chat import chat
from routers.ProjectGuidance import project_abstract
from mangum import Mangum
app = FastAPI(
    title="API Documentation",
    description="API Documentation",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    license={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

handler = Mangum(app)

app.include_router(user_api.router, prefix="/user", tags=["User"])
app.include_router(project_api.router, prefix="/project", tags=["Project"])
app.include_router(asssesment.router, prefix="/interview", tags=["Chatgpt"])
app.include_router(course_api.router, prefix="/course", tags=["Course"])
app.include_router(job_api.router, prefix="/job", tags=["Job"])
app.include_router(blog.router, prefix="/blog", tags=["Blog"])
app.include_router(reportgen.router, prefix="/report", tags=["Reports"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(project_abstract.router, prefix="/projectguidance", tags=['Project Guidance'])

app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "hello world"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
