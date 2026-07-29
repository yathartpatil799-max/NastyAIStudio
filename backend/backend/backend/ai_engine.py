from google import genai
import os

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY not found")

    return genai.Client(api_key=api_key)


def generate_story(prompt):
    client = get_client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
