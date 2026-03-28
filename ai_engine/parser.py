import json
import re

def parse_llm_output(raw_output: str):
    try:
        # Try direct JSON parse
        return json.loads(raw_output)
    
    except:
        try:
            # Extract JSON part using regex
            json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
            if json_match:
                cleaned = json_match.group(0)
                return json.loads(cleaned)
        except:
            pass

    return {
        "error": "Failed to parse response",
        "raw_output": raw_output
    }