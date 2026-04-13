# TestMind AI

An AI-powered test case generator that runs entirely on your local machine. Describe a software feature in plain English and get structured, ready-to-review test cases — no cloud API, no cost, no data leaving your machine.

Built with Python and [Ollama](https://ollama.com), using `phi3` as the default model.

---

## What it does

You give it a feature description like:

```
"User login with email and password"
```

It returns structured test cases like:

```json
{
  "test_cases": [
    {
      "test_case_name": "Successful login with valid credentials",
      "steps": [
        "Navigate to the login page",
        "Enter a valid email address",
        "Enter the correct password",
        "Click the Login button"
      ],
      "expected_result": "User is redirected to the dashboard"
    },
    {
      "test_case_name": "Login fails with wrong password",
      "steps": [
        "Navigate to the login page",
        "Enter a valid email address",
        "Enter an incorrect password",
        "Click the Login button"
      ],
      "expected_result": "An error message is shown and the user stays on the login page"
    }
  ]
}
```

---

## Project Structure

```
testmind-ai/
├── ai_engine/
│   ├── __init__.py
│   ├── llm_client.py       # Sends prompts to Ollama, handles errors
│   ├── parser.py           # Parses LLM output into structured test cases
│   └── prompt_builder.py   # Builds the prompt sent to the model
├── cli/
│   ├── __init__.py
│   └── main.py             # Command-line entry point
├── test_generator/
│   ├── __init__.py
│   └── generator.py        # Orchestrates the full pipeline
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- The `phi3` model pulled in Ollama

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/saqib777/testmind-ai.git
cd testmind-ai
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# On Linux / macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install and start Ollama**

Follow the instructions at [ollama.com](https://ollama.com) for your OS, then:

```bash
ollama serve
```

**5. Pull the phi3 model**

```bash
ollama pull phi3
```

---

## Usage

Run from the repository root:

```bash
python -m cli.main "your feature description here"
```

**Examples:**

```bash
python -m cli.main "User registration with email verification"

python -m cli.main "Shopping cart with add, remove, and quantity update"

python -m cli.main "Password reset via email link"
```

---

## How it works

```
Feature description (plain English)
        |
        v
  prompt_builder.py   — wraps the description in a structured prompt
        |
        v
   llm_client.py      — sends the prompt to Ollama (phi3 model, local)
        |
        v
     parser.py        — extracts test cases from the raw LLM response
        |
        v
  Structured JSON output
```

---

## Changing the model

Open `ai_engine/llm_client.py` and update the `MODEL` constant:

```python
MODEL = "phi3"      # default
# MODEL = "llama3"  # or any model you have pulled in Ollama
```

Any model available in Ollama will work. Larger models generally produce more accurate test cases.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| LLM Runtime | Ollama (local) |
| Default Model | phi3 |
| HTTP Client | requests |
| Interface | CLI |

---

## Author

**Mohammed Saqib**
Final-year MCA student | Aspiring QA Engineer / SDET

[GitHub](https://github.com/saqib777) · [LinkedIn](https://www.linkedin.com/in/mohammed-saqib-b2771836b/)
