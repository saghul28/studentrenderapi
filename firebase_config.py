import pyrebase
import os
firebaseConfig = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": "unnanban-5f098.firebaseapp.com",
  "databaseURL": "https://unnanban-5f098-default-rtdb.firebaseio.com",
  "projectId": "unnanban-5f098",
  "storageBucket": "unnanban-5f098.appspot.com",
  "messagingSenderId": "490434963847",
  "appId": "1:490434963847:web:8738a0065352bd2e314b22",
  "measurementId": "G-HN0935YWY0"
}
firebase = pyrebase.initialize_app(firebaseConfig)
pyredb = firebase.database()
pyreFire = firebase.auth()
#firebase admin
admin_config = {
 "type": "service_account",
  "project_id": "unnanban-5f098",
  "private_key_id": "073581a9438ae09376c77804ba5c859aec70baa7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDBejTEU86tr5cX\nr2m7GAJY52/0nU1mZrfXKXMg+8jLw1jFxsEphke3WON8cfjr8X5ePb2peDCPKwdz\npmRpf8tHvb/DnBqH+jxbAEVgnnB4ki7Df9x9fywy79UMYtywMo7kh+Y5JP72XRId\nBOBvKZP+V6Oghwf+7Ofn4aWCJV4fGIIcGpjTPg8ar3+LtUnj3iHU9yQU4S5LN3yI\ny78SruzJ7Ixl0JAJ76bp4lrcxoPtz08P+XQcQhCmaarzZe+ptWu3pZCXcMY9WYp2\nU6r2LotvuMUK8CEFsq4W1QBbJLMO9PQVIW5x7OY+IkjBZym6tsR4uiHENh0wxHiI\nj42LpyO5AgMBAAECggEAEqEH7iRsqNQYnf71lP5rkXBdWwX/Yx3+UxEKZRFhRN9f\nD5IC3NLxWlHMe5nEwEEdLAlRVv073bkkq0nI7tCPe+2lBnpkIpYhVBjLVVGEHlPi\n/U91JT9Gu/PURXBKdAu2LwJ31CZAB2wwN4uV6ZYtCgcZufXueukILk9Pfp/G94Lb\nS1ozF9ctftYHY6aA1n4AtLSv/dQSgqaTFWEHRTB+LUKd0n/5knyfRNYt+TFChcLJ\nPjMpqcaT01B0h5jhK4Gbnv03XGu5T3uuD3dahAgAVBRxuMrbQitqQWgfAxVx6+r+\nG/hE3oZpAmzjA8EsnoMAIzLWJaKHdBcW0T/sGG+IxQKBgQD1ItFPJ/g5QnLaZyLv\nTAOulG4k6R9Wkbp+hHZlbeP6i+jKothkq3IDaamEnLgwDpflZbgW/2ws2mYLK/Jt\n+kVmixB77YrnR+sHu5swr7pR1/TxH5Y9x0Xb9gpCddkGyC256JddY9+txKhmEeMs\nz5NW1p33VYXtRoA3PWPj1rrPtQKBgQDKDUwRpuFfgSzNzlD/cfVRrtiqhfMPLvEk\nRnn6VA9hnSrU3/6bV0L5zYIFU1Oufe4ImCfAAHpsUNNNgNMLsftuHKKd1O2PO36d\nYJHghhC8QxOQXMyF8cXxkOtXml3WZH+aCjPibeT+wGpCPW2ZWtcNHJlJW3D3kfd2\nO4Lpo5MedQKBgHa/RguFPi5mrQJ1gavP89ynFHAW6dJix6ev/TaHNC/ThJJcrlyd\n3J4gmjiePm8xMo2yZ6nkU3+q0FHLGSYDXYkeBn8yA96jrQvS6ot8JNKuvX3sojgN\nBx9VoYSuV9J8OAJd1K0ty1X+9OB0+8piR2qCjoUYzcayJzwbJf9hrp8dAoGAKTXz\nGPqXpzoaoFN/c8qThbiK2qT9gVBKwOJbCLLSfE9pKAgTzy1KLNc8uMdZHxLyVPBr\n0x6F2cfWgU1QPmdr5/aROG3wkjFJTuIeftP5X9yyhdRXps48WFv9lF2Y3BydZhbE\npF9TwJ4QTjhnPUso57S4kxzCesxb09KpjeveGu0CgYBqZcQTTiIsClhkNtRy+1n0\nE6TqFFBaj9NI5aRxhk2sTLmaCcD90mnQmy2Z280iq6o8xO/lOt1i7Fxo5U5oVRuT\nmGYryEK+pIrFMe3JC+TwuEzRSUXdrnBhm/628KDdLPucRSPtynlOBncXBK5Iy8cY\nbjCb/bRrFbWAlfrr6DLHmA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-urcqi@unnanban-5f098.iam.gserviceaccount.com",
  "client_id": "101556570912181703611",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-urcqi%40unnanban-5f098.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate(admin_config)
fireadmin = firebase_admin.initialize_app(cred)

# import pyrebase

# firebaseConfig = {

#   "apiKey": "AIzaSyAMav1FC8U-1iI7_zgjExy_D8KnNqjLH3c",

#   "authDomain": "unnanban-5f098.firebaseapp.com",

#   "databaseURL": "https://unnanban-5f098-default-rtdb.firebaseio.com",

#   "projectId": "unnanban-5f098",

#   "storageBucket": "unnanban-5f098.appspot.com",

#   "messagingSenderId": "490434963847",

#   "appId": "1:490434963847:web:8738a0065352bd2e314b22",

#   "measurementId": "G-HN0935YWY0"

# }

# firebase = pyrebase.initialize_app(firebaseConfig)

# pyredb = firebase.database()
#"AIzaSyAMav1FC8U-1iI7_zgjExy_D8KnNqjLH3c"
# pyreFire = firebase.auth()

# #firebase admin
# admin_config = {
#  "type": "service_account",
#   "project_id": "unnanban-5f098",
#   "private_key_id": "073581a9438ae09376c77804ba5c859aec70baa7",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDBejTEU86tr5cX\nr2m7GAJY52/0nU1mZrfXKXMg+8jLw1jFxsEphke3WON8cfjr8X5ePb2peDCPKwdz\npmRpf8tHvb/DnBqH+jxbAEVgnnB4ki7Df9x9fywy79UMYtywMo7kh+Y5JP72XRId\nBOBvKZP+V6Oghwf+7Ofn4aWCJV4fGIIcGpjTPg8ar3+LtUnj3iHU9yQU4S5LN3yI\ny78SruzJ7Ixl0JAJ76bp4lrcxoPtz08P+XQcQhCmaarzZe+ptWu3pZCXcMY9WYp2\nU6r2LotvuMUK8CEFsq4W1QBbJLMO9PQVIW5x7OY+IkjBZym6tsR4uiHENh0wxHiI\nj42LpyO5AgMBAAECggEAEqEH7iRsqNQYnf71lP5rkXBdWwX/Yx3+UxEKZRFhRN9f\nD5IC3NLxWlHMe5nEwEEdLAlRVv073bkkq0nI7tCPe+2lBnpkIpYhVBjLVVGEHlPi\n/U91JT9Gu/PURXBKdAu2LwJ31CZAB2wwN4uV6ZYtCgcZufXueukILk9Pfp/G94Lb\nS1ozF9ctftYHY6aA1n4AtLSv/dQSgqaTFWEHRTB+LUKd0n/5knyfRNYt+TFChcLJ\nPjMpqcaT01B0h5jhK4Gbnv03XGu5T3uuD3dahAgAVBRxuMrbQitqQWgfAxVx6+r+\nG/hE3oZpAmzjA8EsnoMAIzLWJaKHdBcW0T/sGG+IxQKBgQD1ItFPJ/g5QnLaZyLv\nTAOulG4k6R9Wkbp+hHZlbeP6i+jKothkq3IDaamEnLgwDpflZbgW/2ws2mYLK/Jt\n+kVmixB77YrnR+sHu5swr7pR1/TxH5Y9x0Xb9gpCddkGyC256JddY9+txKhmEeMs\nz5NW1p33VYXtRoA3PWPj1rrPtQKBgQDKDUwRpuFfgSzNzlD/cfVRrtiqhfMPLvEk\nRnn6VA9hnSrU3/6bV0L5zYIFU1Oufe4ImCfAAHpsUNNNgNMLsftuHKKd1O2PO36d\nYJHghhC8QxOQXMyF8cXxkOtXml3WZH+aCjPibeT+wGpCPW2ZWtcNHJlJW3D3kfd2\nO4Lpo5MedQKBgHa/RguFPi5mrQJ1gavP89ynFHAW6dJix6ev/TaHNC/ThJJcrlyd\n3J4gmjiePm8xMo2yZ6nkU3+q0FHLGSYDXYkeBn8yA96jrQvS6ot8JNKuvX3sojgN\nBx9VoYSuV9J8OAJd1K0ty1X+9OB0+8piR2qCjoUYzcayJzwbJf9hrp8dAoGAKTXz\nGPqXpzoaoFN/c8qThbiK2qT9gVBKwOJbCLLSfE9pKAgTzy1KLNc8uMdZHxLyVPBr\n0x6F2cfWgU1QPmdr5/aROG3wkjFJTuIeftP5X9yyhdRXps48WFv9lF2Y3BydZhbE\npF9TwJ4QTjhnPUso57S4kxzCesxb09KpjeveGu0CgYBqZcQTTiIsClhkNtRy+1n0\nE6TqFFBaj9NI5aRxhk2sTLmaCcD90mnQmy2Z280iq6o8xO/lOt1i7Fxo5U5oVRuT\nmGYryEK+pIrFMe3JC+TwuEzRSUXdrnBhm/628KDdLPucRSPtynlOBncXBK5Iy8cY\nbjCb/bRrFbWAlfrr6DLHmA==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-urcqi@unnanban-5f098.iam.gserviceaccount.com",
#   "client_id": "101556570912181703611",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-urcqi%40unnanban-5f098.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }


# import firebase_admin

# from firebase_admin import credentials


# cred = credentials.Certificate(admin_config)

# fireadmin = firebase_admin.initialize_app(cred)

