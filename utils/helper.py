import openai, os

openai.api_key = os.environ.get("OPENAI_API_KEY")

# # Define a function to generate answers using GPT-3
def generate_answer(question):
    if not openai.api_key:
        return "Error: API key is missing."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Q: {question}\nA:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        return f"An error occurred: {e}"