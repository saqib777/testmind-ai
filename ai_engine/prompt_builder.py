def build_prompt(feature_description: str) -> str:
    return f"""
You are a software test engineer.

Generate structured test cases in STRICT JSON format.

Feature:
{feature_description}

Rules:
- Output MUST be valid JSON
- No explanations, only JSON
- Include positive, negative, and edge cases

Format:
[
  {{
    "test_case_id": "TC001",
    "test_case_name": "Short name",
    "steps": ["step1", "step2"],
    "expected_result": "Expected result",
    "priority": "High/Medium/Low"
  }}
]
"""