from google import genai
from config import config_obj

def get_gemini_client():
    return genai.Client(api_key=config_obj.gemini_api_key)

def ask_gemini(prompt: str):
    client = get_gemini_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

