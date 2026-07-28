from fastapi import APIRouter
from schemas import ChatRequest
from services import call_gemini, call_groq
from router_logic import select_provider
import asyncio

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    tasks = []

    if "gemini" in request.providers:
        tasks.append(call_gemini(request.prompt))

    if "groq" in request.providers:
        tasks.append(call_groq(request.prompt))

    if not tasks:
        return {
            "error": "Please select at least one provider: gemini or groq"
        }

    result = await asyncio.gather(*tasks)

    return {
        "responses": result
    }


@router.post("/auto-chat")
async def auto_chat(request: ChatRequest):

    provider = select_provider(request.prompt)

    if provider == "gemini":
        result = await call_gemini(request.prompt)
    else:
        result = await call_groq(request.prompt)

    return {
        "selected_provider": provider,
        "response": result
    }


@router.get("/")
async def home():
    return {
        "message": "Multi LLM Gateway is Running "
    }