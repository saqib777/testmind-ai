from ai_engine.prompt_builder import build_prompt
from ai_engine.llm_client import generate_from_llm

def generate_test_cases(feature_description: str) -> str:
    prompt = build_prompt(feature_description)
    response = generate_from_llm(prompt)
    return response