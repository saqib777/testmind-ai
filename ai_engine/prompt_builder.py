"""
ai_engine/prompt_builder.py

Constructs the prompt that is sent to the LLM.
The format here directly determines how well the parser can extract test cases.
"""


def build_prompt(feature_description: str) -> str:
    """
    Build a structured prompt for test case generation.

    Args:
        feature_description: Plain-English description of the feature to test.

    Returns:
        A formatted prompt string ready to send to the LLM.
    """
    return f"""You are a senior software test engineer.

Generate between 3 and 5 test cases for the feature described below.

Use this exact format for every test case — do not deviate:

Test Case 1:
Name: <short descriptive name>
Steps:
- <step 1>
- <step 2>
- <step 3>
Expected Result: <what should happen>

Test Case 2:
Name: <short descriptive name>
Steps:
- <step 1>
- <step 2>
Expected Result: <what should happen>

(continue for all test cases)

Rules:
- Every test case must have a Name, at least one Step, and an Expected Result.
- Do not add any commentary, explanation, or text outside the test case blocks.
- Number the test cases sequentially starting from 1.

Feature to test:
{feature_description}
"""
