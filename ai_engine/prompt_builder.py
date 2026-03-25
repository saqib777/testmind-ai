def build_prompt(feature_description: str) -> str:
    return f"""
You are a senior QA engineer.

Generate test cases in STRICT JSON format.

Feature:
{feature_description}

Rules:
- Return ONLY JSON
- No explanations
- No extra text

Format:
[
  {{
    "title": "Test case title",
    "steps": ["step1", "step2"],
    "expected_result": "expected outcome"
  }}
]
"""