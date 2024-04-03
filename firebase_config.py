import pyrebase
import os
from dotenv import load_dotenv
import base64
load_dotenv(".env")


firebaseConfig = {
  "apiKey": os.getenv('API_KEY'),
  "authDomain": os.getenv("AUTH_DOMAIN"),
  "databaseURL": os.getenv( 'DATABASE_URL' ),
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket": os.getenv("STORAGE_BUCKET"),
  "messagingSenderId":os.getenv("MESSAGING_SENDER_ID"),
  "appId":os.getenv("APP_ID"),
  "measurementId": os.getenv("MEASUREMENT_ID"),
}

firebase = pyrebase.initialize_app(firebaseConfig)
pyredb = firebase.database()
pyreFire = firebase.auth()

admin_config = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key" : os.environ["PRIVATE_KEY"],
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}

print(os.getenv("PRIVATE_KEY"))

import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate(admin_config)
fireadmin = firebase_admin.initialize_app(cred)

