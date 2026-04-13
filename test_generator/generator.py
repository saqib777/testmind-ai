"""
test_generator/generator.py

Orchestrates the test generation pipeline:
    1. Build a prompt from the feature description
    2. Send the prompt to the LLM
    3. Parse and return structured test cases
"""

from ai_engine.prompt_builder import build_prompt
from ai_engine.llm_client import generate_from_llm
from ai_engine.parser import parse_llm_output


def generate_test_cases(feature_description: str) -> dict:
    """
    Generate structured test cases for a given feature description.

    Args:
        feature_description: Plain-English description of the feature to test.

    Returns:
        A dict with key "test_cases" containing a list of structured test case dicts.
    """
    prompt = build_prompt(feature_description)
    raw_response = generate_from_llm(prompt)
    return parse_llm_output(raw_response)
