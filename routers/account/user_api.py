from fastapi import APIRouter, Depends, HTTPException, Header, Request
from pydantic import BaseModel
from requests import HTTPError
from firebase_config import pyreFire, pyredb
from firebase_admin import auth

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    email = request.email
    password = request.password
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and Password are required")

    try:
       
        user =pyreFire.sign_in_with_email_and_password(email, password)
       
        
        user_info = pyreFire.get_account_info(user['idToken'])
        id_Token = user['idToken']
        print(user_info)
        # user = auth.get_user_by_email(email)
       
       
        if not user_info.get('users'):
            raise HTTPException(status_code=400, detail="No user information found")
        
        
       
        # Get the first user
        first_user = user_info['users'][0]

        username = first_user.get("displayName", None)
        if not username:
            raise HTTPException(status_code=400, detail="Username not found")
        
        # email_verified = first_user.get("emailVerified", False)
        
        # # If email is not verified, send verification email
        # if not email_verified:
        #     pyreFire.send_email_verification(user['idToken'])
        #     raise HTTPException(status_code=400, detail="Verification link sent! Please verify your email")
        
        
        return {"message":"logged in","token":id_Token, "username": username},
    
    except HTTPError as e:
        error_json = e.args[0].response.json()
        error_message = error_json.get('error', {}).get('message', '')
        raise HTTPException(status_code=400, detail=error_message.lower())
    
class SignUpRequest(BaseModel):
    username:str
    email: str
    password: str
    phone_number:int
    location:str

@router.post("/signup")
async def signup(request: SignUpRequest):
    try:
        user = pyreFire.create_user_with_email_and_password(email=request.email, password=request.password)
        print(request)
        id_token = user['idToken']
        local_id = user['localId']
        # idtoken = pyreFire.send_email_verification(user['id_token'])
        pyreFire.update_profile(id_token,display_name=request.username)
        
    except HTTPError as e:
        error_json = e.args[0].response.json()
        error_message = error_json.get('error', {}).get('message', '')
        if error_message:
            raise HTTPException(status_code=400, detail=error_message.lower())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    user_data = {
        'username':request.username,
        'email': request.email,
        'phone_number': request.phone_number,
        'location':request.location
    }
    try:
        pyredb.child("users").child(user['localId']).set(user_data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "User created successfully"}

class PasswordResetRequest(BaseModel):
    email: str

@router.post("/password-reset")
async def password_reset(request: PasswordResetRequest):
    email = request.email
     
    try:
        auth.get_user_by_email(email)
        pyreFire.send_password_reset_email(email)
        return {"message": "Password Reset Link sent"}
    except auth.UserNotFoundError as e:
        raise HTTPException(status_code=400, detail="User not found")
    except HTTPError as e:
        error_json = e.args[0].response.json()
        error_message = error_json.get('error', {}).get('message', '')
        raise HTTPException(status_code=400, detail=error_message.lower())

# @router.post('/validate_token')
def validate_token(Authorization: str = Header(...)):
    try:
        token = Authorization.split(" ")[1] 
        
        user = auth.verify_id_token(token)
        user_uid = user['uid']
        
        return {"custom_token": user_uid}  # Return the custom token
    except auth.InvalidIdTokenError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    except auth.ExpiredIdTokenError:
        raise HTTPException(status_code=401, detail="Expired authentication token")
