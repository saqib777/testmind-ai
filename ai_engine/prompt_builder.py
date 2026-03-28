def build_prompt(feature_description: str) -> str:
    return f"""
You are a software test engineer.

Generate test cases in STRICT JSON format.

Rules:
- Output MUST be valid JSON
- DO NOT truncate output
- DO NOT leave incomplete fields
- DO NOT include explanations
- Ensure JSON is complete and closed properly

Feature:
{feature_description}

Output format:
{{
  "test_cases": [
    {{
      "test_case_name": "string",
      "steps": ["step1", "step2"],
      "expected_result": "string"
    }}
  ]
}}
"""