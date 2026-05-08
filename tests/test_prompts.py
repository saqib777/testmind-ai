import pytest
from prompts import (
    get_test_case_prompt,
    get_boundary_prompt,
    get_security_prompt,
    get_api_test_prompt,
)


class TestTestCasePrompt:
    def test_contains_feature(self):
        prompt = get_test_case_prompt("User login")
        assert "User login" in prompt

    def test_contains_count(self):
        prompt = get_test_case_prompt("Login", count=5)
        assert "5" in prompt

    def test_default_count(self):
        prompt = get_test_case_prompt("Login")
        assert "8" in prompt

    def test_contains_json_schema(self):
        prompt = get_test_case_prompt("Login")
        assert '"id"'       in prompt
        assert '"title"'    in prompt
        assert '"type"'     in prompt
        assert '"priority"' in prompt
        assert '"steps"'    in prompt

    def test_context_included(self):
        prompt = get_test_case_prompt("Login", context="Mobile app only")
        assert "Mobile app only" in prompt

    def test_no_context_clean(self):
        prompt = get_test_case_prompt("Login")
        assert "Additional context" not in prompt

    def test_scenario_types_mentioned(self):
        prompt = get_test_case_prompt("Login")
        for term in ["positive","negative","boundary","edge"]:
            assert term.lower() in prompt.lower()


class TestBoundaryPrompt:
    def test_contains_feature(self):
        prompt = get_boundary_prompt("Age input field")
        assert "Age input field" in prompt

    def test_mentions_boundary_concepts(self):
        prompt = get_boundary_prompt("Field")
        for concept in ["minimum","maximum","empty"]:
            assert concept.lower() in prompt.lower()

    def test_count_specified(self):
        prompt = get_boundary_prompt("Field")
        assert "6" in prompt


class TestSecurityPrompt:
    def test_contains_feature(self):
        prompt = get_security_prompt("Login form")
        assert "Login form" in prompt

    def test_mentions_attack_types(self):
        prompt = get_security_prompt("Form")
        assert "SQL injection" in prompt
        assert "XSS" in prompt

    def test_count_specified(self):
        prompt = get_security_prompt("Feature")
        assert "5" in prompt


class TestApiPrompt:
    def test_contains_endpoint(self):
        prompt = get_api_test_prompt("/api/users", "POST")
        assert "/api/users" in prompt
        assert "POST" in prompt

    def test_contains_status_codes(self):
        prompt = get_api_test_prompt("/api/users", "GET")
        for code in ["200","400","401","403","404"]:
            assert code in prompt

    def test_payload_included(self):
        prompt = get_api_test_prompt("/api/login", "POST", '{"email":"test"}')
        assert '"email":"test"' in prompt

    def test_no_payload_clean(self):
        prompt = get_api_test_prompt("/api/users", "GET")
        assert "Request body" not in prompt
