import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env")
    exit()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Say hello in one short sentence."
)

print("Gemini response:")
print(response.text)