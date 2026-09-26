# Bookstore QA Midterm

A small (buggy) online-bookstore application for you to test.

## Layout
```
bookstore_app/      the application (assume nothing is correct)
tests/              your test suite goes here
worked_example/     a complete worked bug -- START HERE (not graded)
ai_review/          the AI-generated test set you audit in Part D3
templates/          FINDINGS.md, AI_USAGE.md, REPORT.md to copy and fill in
.github/workflows/  a starter CI workflow for Part E
pytest.ini          registers the smoke / regression / slow markers
requirements.txt
```

## Setup
```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Start here
Read `worked_example/WALKTHROUGH.md` and run `pytest worked_example/`. It shows
one complete bug hunt -- the failing test, then the fix -- in the format your own
findings should follow.

See the midterm handout (PDF) for the full assignment and marking.
