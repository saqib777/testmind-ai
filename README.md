# TestMind AI

An AI-powered test case generator built with Python, Groq API, and Llama 3.
Enter a feature description and get professional, structured test cases instantly.

---

## Features

- Generates manual test cases from plain English descriptions
- Covers positive, negative, boundary, and edge case scenarios
- Outputs structured test cases with steps, expected results, and priority
- Powered by Llama 3 via Groq free tier — no cost to run
- Command-line interface and Python API

---

## Setup

```bash
git clone https://github.com/saqib777/testmind-ai
cd testmind-ai
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at: https://console.groq.com

---

## Usage

```bash
# CLI
python main.py --feature "User login with email and password"

# With output file
python main.py --feature "Password reset flow" --output test_cases.md

# Specify number of test cases
python main.py --feature "Shopping cart checkout" --count 10
```

---

## Example Output

**Feature:** User login with email and password

| # | Test Case | Type | Priority | Expected Result |
|---|-----------|------|----------|-----------------|
| 1 | Valid login with correct credentials | Positive | High | User logged in successfully |
| 2 | Login with wrong password | Negative | High | Error message shown |
| 3 | Login with empty email | Boundary | Medium | Validation error |
| 4 | Login with SQL injection in email | Security | High | Input sanitized, no login |

---

## Structure

```
testmind-ai/
├── main.py              # CLI entry point
├── generator.py         # Core AI test case generation
├── formatter.py         # Output formatting (Markdown, JSON, CSV)
├── prompts.py           # Prompt templates
├── tests/
│   ├── test_generator.py
│   ├── test_formatter.py
│   └── test_prompts.py
├── examples/
│   └── sample_output.md
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python 3.11
- Groq API (free tier)
- Llama 3 70B
- pytest for testing
- python-dotenv for config

---

## Author

Mohammed Saqib - github.com/saqib777 - Bengaluru, India
SDET / QA Automation Engineer
