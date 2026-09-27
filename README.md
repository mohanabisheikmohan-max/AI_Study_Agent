# StudyAgent AI

A simple AI Agent project built with Flask and Gemini.

## Features
- AI study assistant
- Gemini API
- Tool calling
- Calculator tool
- Current-date tool
- Simple responsive UI

## Run in VS Code

1. Open this folder.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it on Windows:
   `venv\Scripts\activate`
4. Install packages:
   `pip install -r requirements.txt`
5. Open `.env` and replace:
   `PASTE_YOUR_GEMINI_API_KEY_HERE`
   with your Gemini API key.
6. Run:
   `python app.py`
7. Open:
   `http://127.0.0.1:5000`

## Project flow

User -> Flask -> AI Agent -> Gemini
                         -> Calculator Tool
                         -> Date Tool
                         -> Final Answer
