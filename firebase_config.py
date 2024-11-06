import pyrebase
import os
from dotenv import load_dotenv
import json
from firebase_admin import firestore, credentials, initialize_app


# Load environment variables
load_dotenv(".env")

# Pyrebase Configuration for Firebase Authentication and Database
firebaseConfig = {
    "apiKey": os.getenv('API_KEY'),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv('DATABASE_URL'),
    "projectId": os.getenv('PROJECT_ID'),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID"),
}

# Initialize Pyrebase for Realtime Database and Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
pyredb = firebase.database()
pyreFire = firebase.auth()




# Convert the configuration to JSON-compatible format if necessary
cred = credentials.Certificate(json.loads(os.getenv("FIREBASE_SERVICE_KEY")))
fireadmin = initialize_app(cred)
firestoreDb = firestore.client()
