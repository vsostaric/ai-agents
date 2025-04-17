import requests
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    prompt = ""
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "user":
            prompt += f"User: {content}\n"
        elif role == "assistant":
            prompt += f"Assistant: {content}\n"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt.strip(),
            "stream": False
        }
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()
