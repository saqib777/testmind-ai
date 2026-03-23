def build_prompt(feature_description: str) -> str:
    prompt = f"""
Generate detailed manual test cases for the following feature:

Feature: {feature_description}

Format strictly as:

Test Case ID:
Title:
Steps:
Expected Result:

Generate at least 3 test cases.
"""
    return prompt