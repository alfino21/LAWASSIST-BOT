import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Create a client using the API key from the environment
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"