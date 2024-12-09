import pyrebase
import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError

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


# Firebase Admin SDK Configuration for Firestore

cred = credentials.Certificate("D:/studentapi/firebase_service_account.json")
firebase_admin.initialize_app(cred)

# Confirm Firebase Admin SDK initialization
app = firebase_admin.get_app()
print(f"Firebase Admin SDK initialized: {app.name}")

# Initialize Firestore client
firestoreDb = firestore.client()
print("Firestore client initialized successfully.")

