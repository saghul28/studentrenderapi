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

# Firebase Admin SDK Configuration
admin_config = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    # Format the private key properly for Firebase
    "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}

# Convert the configuration to JSON-compatible format if necessary
cred = credentials.Certificate(admin_config)
fireadmin = initialize_app(cred)
firestoreDb = firestore.client()
