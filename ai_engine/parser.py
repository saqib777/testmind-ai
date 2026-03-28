def parse_llm_output(raw_output: str):
    test_cases = []
    current = {}

    lines = raw_output.split("\n")

    for line in lines:
        line = line.strip()

        if line.startswith("Test Case"):
            if current:
                test_cases.append(current)
                current = {}

        elif line.startswith("Name:"):
            current["test_case_name"] = line.replace("Name:", "").strip()

        elif line.startswith("-"):
            current.setdefault("steps", []).append(line.replace("-", "").strip())

        elif line.startswith("Expected Result:"):
            current["expected_result"] = line.replace("Expected Result:", "").strip()

    if current:
        test_cases.append(current)

    return {"test_cases": test_cases}