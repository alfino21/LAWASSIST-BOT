from google import genai
from config import GEMINI_API_KEY

# Use the Client API from google.genai
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite-preview-06-17",
            contents=prompt,
        )
        return (response.text or '').strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
