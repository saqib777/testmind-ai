"""
ai_engine/llm_client.py

Handles communication with the local Ollama API.
Sends a prompt and returns the raw text response from the model.
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"
TIMEOUT_SECONDS = 180


def generate_from_llm(prompt: str) -> str:
    """
    Send a prompt to the local Ollama instance and return the generated text.

    Args:
        prompt: The full prompt string to send to the model.

    Returns:
        The model's text response, or an error string if the request fails.
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 600,
        },
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return "[ERROR] Could not connect to Ollama. Is it running? Try: ollama serve"

    except requests.exceptions.Timeout:
        return f"[ERROR] Ollama timed out after {TIMEOUT_SECONDS} seconds."

    except requests.exceptions.HTTPError as e:
        return f"[ERROR] HTTP error from Ollama: {e.response.status_code} - {e.response.text}"

    except Exception as e:
        return f"[ERROR] Unexpected error: {str(e)}"
