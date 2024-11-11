import openai, os
from openai import OpenAI
from twilio.rest import Client

# Your Twilio credentials
account_sid = os.environ.get("TW_ACCOUNT_SID")
auth_token = os.environ.get("TW_AUTH_TOKEN")
twilio_phone_number = os.environ.get("TW_WA_NUMBER")

client = Client(account_sid, auth_token)

openai.api_key = os.environ.get("OPENAI_API_KEY")


openai_client = OpenAI(
    api_key=openai.api_key,
)

# Define a function to generate answers using GPT-3
def generate_answer(question, logger, model="gpt-3.5-turbo"):
    if not openai.api_key:
        return "Error: API key is missing."

    try:
        logger.info(f"Generating answer for: {question}")

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": question
            }
            ]

        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )
        answer = response.choices[0].message.content

        logger.info(f"Generated answer: {answer}")
        
        return answer
    
    except Exception as e:
        return f"An error occurred: {e}"