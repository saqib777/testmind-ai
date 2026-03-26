import requests

# Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Use a stable model
MODEL = "gemma3:4b"

def generate_from_llm(prompt: str) -> str:
    try:
        print("[DEBUG] Sending request to Ollama...")
        print("[DEBUG] Model:", MODEL)

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "format": "json",  # 🔥 VERY IMPORTANT
                "options": {
                    "temperature": 0.2,
                    "num_predict": 200
                }
            },
            timeout=180
        )

        response.raise_for_status()

        data = response.json()

        print("[DEBUG] Raw response received")

        return data.get("response", "")

    except Exception as e:
        print("[DEBUG] Exception occurred:", str(e))
        return f"[ERROR] Ollama failed: {str(e)}"