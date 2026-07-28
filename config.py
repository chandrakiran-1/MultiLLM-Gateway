from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("gemini_api_key")
GROQ_API_KEY = os.getenv("groq_api_key")