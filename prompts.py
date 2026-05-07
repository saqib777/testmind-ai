# Prompt templates for TestMind AI
# Structured prompts produce consistent, high-quality test cases

def get_test_case_prompt(feature: str, count: int = 8, context: str = "") -> str:
    """
    Build the main prompt for test case generation.

    Designed to produce structured, professional test cases
    covering all scenario types a QA engineer would write.
    """
    context_block = f"\nAdditional context: {context}" if context else ""

    return f"""You are a senior QA Engineer with 10 years of experience.
Generate exactly {count} professional test cases for the following feature.{context_block}

Feature: {feature}

Requirements:
- Cover positive, negative, boundary, and edge cases
- Include at least one security-related test case if applicable
- Each test case must be unique and specific
- Write clear, unambiguous test steps
- Base expected results on standard software behaviour

Return ONLY a JSON array. No preamble, no markdown, no explanation.
Each object must have exactly these fields:
{{
    "id": "TC001",
    "title": "Brief descriptive title",
    "type": "Positive|Negative|Boundary|Edge|Security|Performance",
    "priority": "High|Medium|Low",
    "preconditions": "What must be true before the test",
    "steps": ["Step 1", "Step 2", "Step 3"],
    "expected_result": "What should happen",
    "test_data": "Sample data to use (or N/A)"
}}"""


def get_boundary_prompt(feature: str) -> str:
    """Focused prompt for boundary value analysis only."""
    return f"""You are a QA Engineer specialising in boundary value analysis.
Generate 6 boundary test cases for: {feature}

Focus exclusively on:
- Minimum valid values
- Maximum valid values
- Just below minimum (invalid)
- Just above maximum (invalid)
- Empty/null/zero values
- Extremely large inputs

Return ONLY a JSON array with the same schema as before."""


def get_security_prompt(feature: str) -> str:
    """Focused prompt for security test cases."""
    return f"""You are a security-focused QA Engineer.
Generate 5 security test cases for: {feature}

Cover:
- SQL injection attempts
- XSS (Cross-Site Scripting)
- Authentication bypass attempts
- Privilege escalation
- Input sanitisation failures

Return ONLY a JSON array with the same schema as before."""


def get_api_test_prompt(endpoint: str, method: str, payload: str = "") -> str:
    """Prompt specifically for REST API test case generation."""
    payload_block = f"\nRequest body: {payload}" if payload else ""
    return f"""You are a senior API Test Engineer.
Generate 8 test cases for the following API endpoint.

Endpoint: {method} {endpoint}{payload_block}

Cover:
- Valid request with correct data (200/201)
- Missing required fields (400)
- Invalid data types (400)
- Unauthorised request (401)
- Forbidden resource (403)
- Resource not found (404)
- Duplicate resource if applicable (409)
- Server behaviour under valid edge case

Return ONLY a JSON array with these fields:
{{
    "id": "TC001",
    "title": "Brief title",
    "method": "{method}",
    "endpoint": "{endpoint}",
    "request_body": {{}},
    "headers": {{}},
    "expected_status": 200,
    "expected_response": "Description of expected response body",
    "type": "Positive|Negative|Security|Boundary"
}}"""
