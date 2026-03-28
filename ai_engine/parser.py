import json
import re

def parse_llm_output(raw_output: str):
    try:
        # First attempt: direct parse
        return json.loads(raw_output)

    except:
        try:
            # Extract JSON block
            json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
            if json_match:
                cleaned = json_match.group(0)

                # Fix escaped quotes
                cleaned = cleaned.replace('\\"', '"')

                return json.loads(cleaned)

        except Exception as e:
            return {
                "error": "Failed to parse response",
                "raw_output": raw_output,
                "exception": str(e)
            }

    return {
        "error": "Failed to parse response",
        "raw_output": raw_output
    }