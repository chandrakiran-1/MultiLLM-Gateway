# router_logic.py

def select_provider(prompt: str):

    prompt = prompt.lower()

    coding_words = [
        "code",
        "python",
        "javascript",
        "bug",
        "debug",
        "algorithm",
        "function"
    ]

    for word in coding_words:
        if word in prompt:
            return "groq"

    return "gemini"