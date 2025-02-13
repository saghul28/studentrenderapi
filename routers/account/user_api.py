from fastapi import APIRouter, Depends, HTTPException, Header, Request,Response
from pydantic import BaseModel
from requests import HTTPError
from firebase_config import pyreFire, pyredb
from firebase_admin import auth
from fastapi.responses import JSONResponse

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

api_key_global = None

def get_api_key():
    print(api_key_global)
    return api_key_global


@router.post("/login")
async def login(request: LoginRequest, response: Response):
    global api_key_global  # Declare the global variable

    email = request.email
    password = request.password

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and Password are required")

    try:
        user = pyreFire.sign_in_with_email_and_password(email, password)
        user_info = pyreFire.get_account_info(user['idToken'])
        id_Token = user['idToken']

        if not user_info.get('users'):
            raise HTTPException(status_code=400, detail="No user information found")

        first_user = user_info['users'][0]
        username = first_user.get("displayName", None)
        uid = first_user.get("localId", None)

        # email_verified = first_user.get("emailVerified", False)

        # # If email is not verified, send verification email
        # if not email_verified:
        #     pyreFire.send_email_verification(user['idToken'])
        #     raise HTTPException(status_code=400, detail="Verification link sent! Please verify your email")

        if not username or not uid:
            raise HTTPException(status_code=400, detail="User information is incomplete")

        api_key_global = pyredb.child("Users").child(uid).get().val().get("api_key") # No need for `await`
        print("API Key Retrieved: ", api_key_global)

        return JSONResponse({"message": "Logged in", "token": id_Token, "username": username})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




class SignUpRequest(BaseModel):
    username:str
    email: str
    password: str
    phone_number:int
    location:str
    api_key: str

@router.post("/signup")
async def signup(request: SignUpRequest):
    global api_key_global  # Declare the global variable
    try:
        user = pyreFire.create_user_with_email_and_password(email=request.email, password=request.password)
        api_key_global = request.api_key  # This will update the global variable
        id_token = user['idToken']
        uid = user['localId']
        pyreFire.update_profile(id_token, display_name=request.username)
        pyredb.child("Users").child(uid).set({"api_key":request.api_key})

    except HTTPError as e:
        error_json = e.args[0].response.json()
        error_message = error_json.get('error', {}).get('message', '')
        if error_message:
            raise HTTPException(status_code=400, detail=error_message.lower())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    user_data = {
        'username': request.username,
        'email': request.email,
        'phone_number': request.phone_number,
        'location': request.location
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


def get_uid_from_cookie(request: Request):
    uid = request.cookies.get("uid")
    if not uid:
        raise HTTPException(status_code=401, detail="User is not logged in")
    return uid


# {
#   "username": "javeed",
#   "email": "javeed@gmail.com",
#   "password": "javeed",
#   "phone_number": 0,
#   "location": "string",
#   "api_key": "AIzaSyBaJInUzY9hvQYVfr2TXUvY5UH7WmzjGsI"
# }