import json


def parse_llm_output(response: str):
    try:
        # Clean response (LLMs sometimes add junk)
        cleaned = response.strip()

        # Find JSON start
        start = cleaned.find("[")
        end = cleaned.rfind("]") + 1

        json_str = cleaned[start:end]

        return json.loads(json_str)

    except Exception as e:
        return {
            "error": "Failed to parse response",
            "raw_output": response,
            "exception": str(e)
        }