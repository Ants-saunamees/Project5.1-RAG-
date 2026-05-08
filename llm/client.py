import requests

def chat_with_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-r1:1.5b",
            "prompt": prompt,
            "stream": False
        }

    )

    data = response.json()

    if "response" in data:
        return data["response"]

    # If Ollama returned an error, show it clearly
    if "error" in data:
        return f"LLM Error: {data['error']}"

    return "Unknown LLM error"
