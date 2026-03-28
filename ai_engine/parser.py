def build_prompt(feature_description: str) -> str:
    return f"""
You are a software test engineer.

Generate 3 to 5 test cases.

Format strictly like this:

Test Case 1:
Name: ...
Steps:
- step 1
- step 2
Expected Result: ...

Test Case 2:
...

Feature:
{feature_description}
"""