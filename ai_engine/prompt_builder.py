def build_prompt(feature_description: str) -> str:
    return f"""
You are a QA engineer.

Generate test cases for the following feature:

Feature: {feature_description}

Return STRICTLY in JSON format like this:

[
  {{
    "id": "TC_01",
    "title": "Test title",
    "steps": ["step1", "step2"],
    "expected_result": "expected outcome"
  }}
]

Do not add any explanation. Only return JSON.
"""