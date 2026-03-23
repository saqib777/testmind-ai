from ai_engine.prompt_builder import build_prompt
from ai_engine.llm_client import generate_from_llm
from ai_engine.parser import parse_llm_output


def generate_test_cases(feature_description: str):
    prompt = build_prompt(feature_description)

    raw_response = generate_from_llm(prompt)

    parsed = parse_llm_output(raw_response)

    return parsed