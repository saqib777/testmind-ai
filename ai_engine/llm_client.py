import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"   # or "gemma3:4b" if you prefer


def generate_from_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "")

    except Exception as e:
        return f"[ERROR] Ollama failed: {str(e)}"