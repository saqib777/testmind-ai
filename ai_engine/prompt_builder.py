def build_prompt(feature_description: str) -> str:
    return f"""
You are a software test engineer.

Generate test cases in JSON format.

Feature:
{feature_description}

Instructions:
- Give 3 to 5 test cases
- Include positive and negative scenarios
- Keep output simple and valid JSON
- Do not include explanations

Output format:
[
  {{
    "test_case_name": "Short name",
    "steps": ["step1", "step2"],
    "expected_result": "Expected result"
  }}
]
"""