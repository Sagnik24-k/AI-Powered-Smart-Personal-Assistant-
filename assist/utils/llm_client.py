import requests
import json

USE = "openrouter"  


OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "meta-llama/llama-3.3-70b-instruct:free" 



OLLAMA_MODEL = "llama3.2:3b"  
OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_llm(prompt):
    if USE == "openrouter":
        return ask_openrouter(prompt)
    elif USE == "ollama":
        return ask_ollama(prompt)
    return "LLM backend not configured."


def ask_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 80
    }

    response = requests.post(url, headers=headers, json=data)
    
    try:
        return response.json()["choices"][0]["message"]["content"].strip()
    except:
        return "LLM error."


def ask_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OLLAMA_URL, json=payload)

    try:
        return response.json()["message"]["content"].strip()
    except:
        return "Local LLM error."
