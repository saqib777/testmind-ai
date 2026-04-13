"""
cli/main.py

Command-line entry point for TestMind AI.

Usage:
    python -m cli.main "your feature description here"

Example:
    python -m cli.main "User login with email and password"
"""

import sys
import json

# Allow running from repo root: python -m cli.main
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_generator.generator import generate_test_cases


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m cli.main \"<feature description>\"")
        print("Example: python -m cli.main \"User login with email and password\"")
        sys.exit(1)

    feature_description = " ".join(sys.argv[1:])

    print(f"\n[TestMind AI] Generating test cases for: {feature_description!r}\n")

    result = generate_test_cases(feature_description)

    if "error" in result:
        print(f"[ERROR] {result['error']}")
        sys.exit(1)

    test_cases = result.get("test_cases", [])

    if not test_cases:
        print("[WARN] No test cases were parsed from the LLM output.")
        print("       Try rephrasing your feature description.")
        sys.exit(1)

    print(f"[TestMind AI] {len(test_cases)} test case(s) generated:\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
