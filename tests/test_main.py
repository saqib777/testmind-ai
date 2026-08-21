# CLI tests for main.py
# Uses subprocess to test the CLI entry point end-to-end (mocked)

import pytest
import json
from unittest.mock import patch, MagicMock
from io import StringIO

SAMPLE_TC = [
    {
        "id": "TC001",
        "title": "Valid login",
        "type": "Positive",
        "priority": "High",
        "preconditions": "User registered",
        "steps": ["Open page", "Enter credentials", "Click login"],
        "expected_result": "Logged in successfully",
        "test_data": "user@test.com / Test@1234"
    }
]


@pytest.fixture
def mock_generator():
    with patch("main.TestCaseGenerator") as MockGen:
        instance = MagicMock()
        instance.generate.return_value = SAMPLE_TC
        instance.generate_boundary.return_value = SAMPLE_TC
        instance.generate_security.return_value = SAMPLE_TC
        instance.generate_comprehensive.return_value = {
            "standard": SAMPLE_TC,
            "boundary": SAMPLE_TC,
            "security": SAMPLE_TC,
        }
        MockGen.return_value = instance
        yield instance


class TestCLIArgParsing:

    def test_feature_required(self):
        import argparse
        from main import build_parser
        parser = build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args([])   # no --feature provided

    def test_feature_accepted(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login flow"])
        assert args.feature == "Login flow"

    def test_count_default(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login"])
        assert args.count == 8

    def test_count_override(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login", "--count", "5"])
        assert args.count == 5

    def test_format_default(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login"])
        assert args.format == "markdown"

    def test_format_choices(self):
        from main import build_parser
        parser = build_parser()
        for fmt in ["markdown", "json", "csv", "summary"]:
            args = parser.parse_args(["--feature", "Login", "--format", fmt])
            assert args.format == fmt

    def test_boundary_flag(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login", "--boundary"])
        assert args.boundary == True

    def test_security_flag(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login", "--security"])
        assert args.security == True

    def test_comprehensive_flag(self):
        from main import build_parser
        parser = build_parser()
        args   = parser.parse_args(["--feature", "Login", "--comprehensive"])
        assert args.comprehensive == True


class TestOutputFormats:

    def test_markdown_output_contains_title(self, mock_generator, capsys):
        with patch("main.TestCaseGenerator", return_value=mock_generator):
            from main import main
            with patch("sys.argv", ["main.py", "--feature", "Login flow"]):
                main()
        captured = capsys.readouterr()
        assert "TC001" in captured.out or "Valid login" in captured.out

    def test_json_format_is_valid_json(self, mock_generator):
        from formatter import to_json
        output = to_json(SAMPLE_TC)
        parsed = json.loads(output)
        assert parsed[0]["id"] == "TC001"

    def test_csv_format_has_header(self, mock_generator):
        from formatter import to_csv
        output = to_csv(SAMPLE_TC)
        assert "id" in output.split("\n")[0]
        assert "TC001" in output
