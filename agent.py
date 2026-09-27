import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import calculator, current_date

# Load .env
load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please add your API key to the .env file."
    )

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are StudyAgent, an AI study assistant.

Your job is to help students with:
- Learning
- Python programming
- AI and Machine Learning
- Project ideas
- Exam preparation
- Technical explanations
- Interview preparation

You have access to tools for:
1. Calculator
2. Current date

Use a tool when it is genuinely useful.

Give simple, clear and structured answers.

If the question is unrelated to study, programming,
AI, technology or education, politely explain that
you mainly support study and technical topics.
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