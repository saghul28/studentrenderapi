from fastapi import APIRouter, Form, Depends
from pydantic import BaseModel
from fastapi.responses import  JSONResponse


from routers.account.user_api import get_uid_from_cookie

router = APIRouter() 

class GetAPIFromUser(BaseModel):
    apiKey:str


@router.post("/get_api")
def getapi(apiGet : GetAPIFromUser,uid:str = Depends(get_uid_from_cookie)):
    print("ssample")
    return JSONResponse({"uid":uid,"api":apiGet.apiKey})
    
    