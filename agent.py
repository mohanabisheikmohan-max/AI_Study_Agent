import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

from tools import calculator, current_date

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing.")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are StudyAgent, an AI study assistant.

Help students with:
- Python
- AI
- Machine Learning
- Programming
- Projects
- Exam preparation
- Technical explanations
- Interview preparation

You have two tools:
1. Calculator
2. Current date

Use tools when useful.

Give simple and structured answers.
"""

def run_agent(question):

    response = client.models.generate_content(
        model=MODEL,
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[calculator, current_date],
            temperature=0.3,
        ),
    )

    return response.text