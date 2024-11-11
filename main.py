from fastapi import FastAPI, Form, Request
from fastapi.responses import Response

from mangum import Mangum

from utils.helper import *

from twilio.twiml.messaging_response import MessagingResponse

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello World Again - Enforced application/xml response!"}

@app.get("/hi")
async def hi():
    return {"message": "Testing Get Route - Hello from the other side!"}

@app.post("/name")
async def get_name(name: str = Form(...)):
    return {"message": f"Hello {name}! This is a test post route."}

@app.post("/message")
async def answer(request: Request):
    
    form_data = await request.form()

    msg_body = form_data.get("Body")

    logger.info(f"Received message: {msg_body}")

    reciever = form_data.get("To")

    logger.info(f"Receiver: {reciever}")

    answer = generate_answer(question=msg_body, logger=logger)

    resp = MessagingResponse()
    resp.message(answer)

    logger.info(f"Sending message: {str(resp)}")

    return Response(content=str(resp), media_type="application/xml")