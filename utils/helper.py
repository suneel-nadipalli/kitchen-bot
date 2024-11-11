import openai, os
from twilio.rest import Client

# Your Twilio credentials
account_sid = os.environ.get("TW_ACCOUNT_SID")
auth_token = os.environ.get("TW_AUTH_TOKEN")
twilio_phone_number = os.environ.get("TW_WA_NUMBER")

client = Client(account_sid, auth_token)

openai.api_key = os.environ.get("OPENAI_API_KEY")

# def send_message(body_text, sender, receiver):
#     client.messages.create(
#         from_=f"whatsapp:{twilio_phone_number}", 
#         body=body_text, 
#         to=f"whatsapp:{receiver}"
#     )

# Define a function to generate answers using GPT-3
def generate_answer(question, logger):
    if not openai.api_key:
        return "Error: API key is missing."

    try:
        logger.info(f"Generating answer for: {question}")

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Q: {question}\nA:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        answer = response.choices[0].text.strip()

        logger.info(f"Generated answer: {answer}")
        
        return answer
    
    except Exception as e:
        return f"An error occurred: {e}"