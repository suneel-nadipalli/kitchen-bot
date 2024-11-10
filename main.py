from fastapi import FastAPI, Request
from mangum import Mangum
from twilio.twiml.messaging_response import MessagingResponse
from utils.helper import *

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello World Again 2!"}

@app.post("/answer")
async def answer(request: Request):
    question = await request.form().get("Body")
    answer = generate_answer(question)
    # response = MessagingResponse()
    # response.message(answer)
    return {"message": answer}