from services import call_groq
import asyncio

result = asyncio.run(
    call_groq("What is FastAPI?")
)

print(result)