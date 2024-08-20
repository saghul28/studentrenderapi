from fastapi import APIRouter, Depends, HTTPException, Header, Request
from pydantic import BaseModel
import razorpay

RAZORPAY_KEY_ID = "your_razorpay_key_id"
RAZORPAY_SECRET_KEY = "your_razorpay_secret_key"

razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY))

class PaymentRequest(BaseModel):
    amount: int
    currency: str
    receipt: str

@app.post("/create_order/")
def create_order(payment_request: PaymentRequest):
    try:
        data = {"amount": 500, "currency": "INR", "receipt": "order_rcptid_11"}
        payment = razorpay_client.order.create(data=data)
        return {"order_id": razorpay_client["id"], "status": razorpay_client["status"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

