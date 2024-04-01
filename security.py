from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Firebase authentication function
async def get_current_user(id_token: str = Depends(oauth2_scheme)):
    try:
        print({"token":id_token})
        decoded_token = auth.verify_id_token(id_token)
        
        uid = decoded_token['uid']
        
        # Perform additional checks or fetch user info from Firebase if needed
        return uid
    except auth.InvalidIdTokenError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    except auth.ExpiredIdTokenError:
        raise HTTPException(status_code=401, detail="Expired authentication token")