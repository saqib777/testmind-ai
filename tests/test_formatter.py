import pytest
import json
import csv
import io
from formatter import (
    to_markdown, to_json, to_csv,
    to_summary_table, count_by_type, count_by_priority
)

SAMPLE = [
    {
        "id": "TC001",
        "title": "Valid login with correct credentials",
        "type": "Positive",
        "priority": "High",
        "preconditions": "User is registered",
        "steps": ["Open login page", "Enter valid email", "Click submit"],
        "expected_result": "User is redirected to dashboard",
        "test_data": "email: test@test.com, password: Test@123"
    },
    {
        "id": "TC002",
        "title": "Login with wrong password",
        "type": "Negative",
        "priority": "High",
        "preconditions": "User is registered",
        "steps": ["Open login page", "Enter wrong password", "Click submit"],
        "expected_result": "Error message displayed",
        "test_data": "password: wrongpass"
    },
    {
        "id": "TC003",
        "title": "Login with empty email",
        "type": "Boundary",
        "priority": "Medium",
        "preconditions": "None",
        "steps": ["Open login page", "Leave email blank", "Click submit"],
        "expected_result": "Validation error shown",
        "test_data": "email: empty"
    },
]


class TestMarkdown:
    def test_contains_ids(self):
        md = to_markdown(SAMPLE)
        assert "TC001" in md and "TC002" in md

    def test_contains_titles(self):
        md = to_markdown(SAMPLE)
        assert "Valid login" in md

    def test_contains_steps(self):
        md = to_markdown(SAMPLE)
        assert "Open login page" in md

    def test_feature_header(self):
        md = to_markdown(SAMPLE, feature="Login Flow")
        assert "Login Flow" in md

    def test_empty_list(self):
        md = to_markdown([])
        assert "0 test cases" in md

    def test_step_numbering(self):
        md = to_markdown(SAMPLE[:1])
        assert "1. Open login page" in md


class TestJson:
    def test_valid_json(self):
        result = json.loads(to_json(SAMPLE))
        assert len(result) == 3

    def test_preserves_all_fields(self):
        result = json.loads(to_json(SAMPLE))
        assert result[0]["id"] == "TC001"
        assert isinstance(result[0]["steps"], list)

    def test_empty(self):
        assert to_json([]) == "[]"


class TestCsv:
    def test_has_header(self):
        result = to_csv(SAMPLE)
        assert "id,title" in result or "id" in result.split('\n')[0]

    def test_correct_row_count(self):
        result = to_csv(SAMPLE)
        reader = csv.DictReader(io.StringIO(result))
        rows = list(reader)
        assert len(rows) == 3

    def test_steps_joined(self):
        result = to_csv(SAMPLE[:1])
        assert " | " in result

    def test_empty_returns_empty(self):
        assert to_csv([]) == ""


class TestCounts:
    def test_count_by_type(self):
        counts = count_by_type(SAMPLE)
        assert counts["Positive"] == 1
        assert counts["Negative"] == 1
        assert counts["Boundary"] == 1

    def test_count_by_priority(self):
        counts = count_by_priority(SAMPLE)
        assert counts["High"]   == 2
        assert counts["Medium"] == 1

    def test_summary_table_rows(self):
        table = to_summary_table(SAMPLE)
        lines = [l for l in table.split('\n') if l.startswith('|') and '---' not in l]
        assert len(lines) == 4   # header + 3 data rows
