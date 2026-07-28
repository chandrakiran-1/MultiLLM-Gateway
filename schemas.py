from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    prompt: str
    providers: List[str] = ["gemini", "groq"]