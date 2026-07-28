import asyncio
import google.generativeai as genai
from groq import Groq

from config import GEMINI_API_KEY, GROQ_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

groq_client = Groq(api_key=GROQ_API_KEY)


async def call_gemini(prompt: str):

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return {
        "provider": "Gemini",
        "response": response.text
    }


async def call_groq(prompt: str):

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "provider": "Groq",
        "response": response.choices[0].message.content
    }