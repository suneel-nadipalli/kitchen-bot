from fastapi import FastAPI, Form, Request
from mangum import Mangum
from utils.helper import *
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello World Again - Testing messaging v1!"}

@app.post("/message")
async def answer(request: Request):
    
    form_data = await request.form()

    msg_body = form_data.get("Body")

    sender = form_data.get("From")

    reciever = form_data.get("To")

    answer = generate_answer(msg_body)

    send_message(answer, sender, reciever)

    # Generate Twilio response
    resp = MessagingResponse()
    resp.message(answer)

    return str(resp)

    # return {"message": answer}