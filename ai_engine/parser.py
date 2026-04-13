"""
ai_engine/parser.py

Parses the raw LLM text output into a structured list of test cases.

Expected input format per test case:

    Test Case N:
    Name: ...
    Steps:
    - step 1
    - step 2
    Expected Result: ...
"""

import re


def parse_llm_output(raw_output: str) -> dict:
    """
    Parse raw LLM text into a structured dictionary of test cases.

    Args:
        raw_output: The raw string response from the LLM.

    Returns:
        A dict with key "test_cases" containing a list of test case dicts.
        Each test case has: test_case_name, steps (list), expected_result.
    """
    if not raw_output or raw_output.startswith("[ERROR]"):
        return {"test_cases": [], "error": raw_output}

    test_cases = []
    current: dict = {}
    reading_steps = False

    for raw_line in raw_output.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        # Detect start of a new test case block: "Test Case 1:", "Test Case 2:", etc.
        if re.match(r"^Test Case\s+\d+\s*:", line, re.IGNORECASE):
            if current:
                test_cases.append(_finalise(current))
            current = {}
            reading_steps = False
            continue

        if line.lower().startswith("name:"):
            current["test_case_name"] = line[5:].strip()
            reading_steps = False
            continue

        if line.lower() == "steps:":
            current.setdefault("steps", [])
            reading_steps = True
            continue

        if reading_steps and line.startswith("-"):
            step_text = line.lstrip("- ").strip()
            if step_text:
                current.setdefault("steps", []).append(step_text)
            continue

        if line.lower().startswith("expected result:"):
            current["expected_result"] = line[len("expected result:"):].strip()
            reading_steps = False
            continue

    # Append the last block if it exists
    if current:
        test_cases.append(_finalise(current))

    return {"test_cases": test_cases}


def _finalise(tc: dict) -> dict:
    """
    Fill in missing fields with safe defaults before appending a test case.
    """
    return {
        "test_case_name": tc.get("test_case_name", "Unnamed Test Case"),
        "steps": tc.get("steps", []),
        "expected_result": tc.get("expected_result", "Not specified"),
    }
