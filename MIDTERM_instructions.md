# Midterm Project: Testing an Online Bookstore with Pytest

## Automated Software Testing (192-211)

### Overview

Your team is the Quality Assurance (QA) team for a new online bookstore. You
are given the application code -- and it contains bugs. Your job is to design a
testing strategy using smoke, regression, and slow tests, implement it with
pytest markers, and above all, write tests that CATCH the bugs.

This is a group project (3-5 students). Total: 100 marks, plus a 10-mark bonus.

---

## Getting the Code

You start from a template repository your instructor has published on GitHub:
**https://github.com/teaching-git/st211-midterm-bookstore-fall-2026.git**

**Do not push your work back to the instructor's repository.** Make your own
copy, work there, and submit your copy's link.

### Easiest way: "Use this template"
1. Open the instructor's repository link on GitHub.
2. Click the green **Use this template** button -> **Create a new repository**.
3. Name it `st211-midterm-<your-group-name>` and set it to **Private**.
4. Add your instructor as a collaborator (Settings -> Collaborators).
5. Clone YOUR new repository to your computer and start working.

### Alternative: clone and re-push
If the template button is unavailable:
```
git clone https://github.com/teaching-git/st211-midterm-bookstore-fall-2026.git st211-midterm-<group>
cd st211-midterm-<group>
rm -rf .git
git init
git add .
git commit -m "start midterm"
```
Then create an empty repository on your own GitHub account and push to it.

### What is in the repository
```
bookstore_app/      the application (assume nothing is correct!)
  users.py          registration + login
  catalog.py        products + search
  cart.py           cart, checkout, orders, bulk import
tests/
  test_bookstore.py where your tests go
pytest.ini          registers the markers
README.md
```

Install pytest and confirm it runs:
```
pip install pytest
pytest
```

---

## What to Submit

1. Your test suite in `tests/` (committed progressively to your repo).
2. `REPORT.md` -- a written report in README style (Markdown headings and short
   prose), covering Parts A, B, and F.
3. `FINDINGS.md` -- your bug-hunt log: HOW you found each bug (see the FINDINGS
   section below). A template is provided in your repository.
4. `AI_USAGE.md` -- your AI usage declaration and comparison (see the AI section
   below). A template is provided in your repository.
5. Your group's repository URL.

**Work progressively.** Commit as you go, with clear messages. A history of
small commits from several people is expected. A single "upload" commit at the
end from one person is a red flag.

**Name every test's author.** Each test's docstring must say who wrote it, e.g.
`"""Author: Mai. Regression test for the cart-total bug."""` This is how
individual contribution is graded.

---

## Part A: Test Type Foundations (10 marks)

For each of smoke, regression, and slow testing:
- Define it in your own words.
- Explain when it should be run.
- Give 3 examples relevant to this bookstore.

---

## Part B: Classification Challenge (10 marks)

For each scenario, state whether it is a smoke, regression, or slow test (or
more than one), and justify in 2-3 sentences.

1. Verify that users can log in successfully.
2. Verify that a previously fixed discount-calculation bug does not reappear.
3. Verify importing 100,000 products.
4. Verify that checkout works after each deployment.
5. Verify that a bug involving special characters in passwords remains fixed.
6. Verify generating annual sales reports from 10 years of data.

---

## Part C: Smoke and Slow Test Suite (20 marks)

Write REAL, RUNNABLE tests in `tests/test_bookstore.py`.

**Smoke tests (at least 5):** quick checks that core features work at all --
register, login (with a valid simple password), add a product, add to cart,
checkout with a non-empty cart. Mark each `@pytest.mark.smoke`.

**Slow tests (at least 2):** exercise the app with large data, for example
importing tens of thousands of products, or performing many operations in a
loop. Mark each `@pytest.mark.slow`. In a comment, explain what makes it slow.

Marks are for tests that actually run and genuinely check the feature.

---

## Part D: The Bug Hunt -- Regression Tests (25 marks)

The application contains **several bugs**. You are NOT told what they are or
where they live. Your job is to find them by exploring the code and testing how
it actually behaves versus how it SHOULD behave.

**How to hunt:** read each module, think about what each function is supposed to
do, then write a test that checks it. When a function does the wrong thing, your
test will fail -- and you have found a bug.

For EACH bug you find, write a regression test that:
- FAILS while the bug is present (this proves your test truly detects it), then
- PASSES after you fix the bug in `bookstore_app/`.

Mark each test `@pytest.mark.regression`, and in its docstring describe the bug
you found in your own words (what was wrong, and what the correct behaviour is).

**Where to look:** every module (`users.py`, `catalog.py`, `cart.py`) has
something worth checking. Do not stop at the first bug you find -- there are
more than one. The strongest groups will find and catch several.

Marking (per genuine bug you find and handle):
- A regression test that correctly FAILS against the buggy code (proving it
  detects a real bug): 3 marks.
- A correct fix so that same test then PASSES: 2 marks.
Marks accumulate across the bugs you find, up to the 30 for this part. You do
not need to find every bug to score well, but finding more scores higher.

**Tip:** a good bug report in your test docstring names the function, describes
the wrong behaviour you observed, and states what you expected instead.

---

## Part D2: Your Bug-Hunt Log -- FINDINGS.md (10 marks)

Finding a bug is only half the skill; being able to SHOW how you found it is the
other half. As you hunt (Part D), keep a running log in `FINDINGS.md`. A template
is in your repository -- fill in one entry per bug you find.

For each bug, your log entry should record:
- **What you suspected** -- which function, and why you thought it might be wrong.
- **What you did** -- the input you tried, or the test you wrote to check it.
- **What you observed** -- the actual (wrong) result.
- **What you expected** -- the correct behaviour.
- **The fix** -- what you changed to correct it.

Write it like a detective's notebook, in your own words. A good log shows the
messy, real path to the bug (including dead ends). Marks are for genuine,
specific, first-person documentation -- not a tidy after-the-fact summary.

This part MUST be done as you go. Complete each entry BEFORE you move to the AI
comparison below -- the whole point is to capture YOUR reasoning first.

---

## Part D3: AI Usage Declaration and Comparison (15 marks)

Modern testers use AI tools. This part is not about avoiding them -- it is about
using them HONESTLY and CRITICALLY. Record everything in `AI_USAGE.md` (template
provided).

### D3.1 -- Declaration (required)
List every AI tool your group used anywhere in this project (for tests, for the
report, for understanding the code), and briefly how you used each. Declaring is
required; using AI is allowed. Undeclared AI use found during grading is treated
as an academic-honesty issue.

### D3.2 -- The comparison (do this AFTER your own hunt)
You have already found and logged bugs yourselves (Part D2). Now run the SAME
bug-hunt task through **at least two different AI tools** (for example Claude,
Gemini, ChatGPT, Copilot -- any two distinct ones). Give each the app code and
ask it to find bugs and write tests.

Record what each AI produced, then build a comparison table like this:

| Bug (in your words) | We found it? | AI #1 found it? | AI #2 found it? | Was each AI's test CORRECT? |
| --- | --- | --- | --- | --- |
| (e.g. total skips last item) | Yes | Yes | No | AI#1: correct; AI#2: n/a |
| ... | ... | ... | ... | ... |

The last column is the most important. An AI often produces a test that LOOKS
right but does not actually detect the bug (it passes even against the buggy
code), or invents a "bug" that is not real. For each AI test, state whether it
genuinely catches the bug, and how you verified that.

### D3.3 -- Your verdict (the graded core)
In a few short paragraphs:
- Where did YOUR human judgement beat the AIs? (bugs you found that they missed,
  or AI tests you had to correct.)
- Where did an AI catch something you had missed?
- What did this teach you about relying on AI to write tests?

Marks are for the QUALITY of your critical evaluation -- specifically the D3.2
"was the AI correct?" analysis and the D3.3 verdict -- not for how many AIs you
tried or which one "won". A group that blindly reports AI output without
checking whether the tests actually work will score poorly here.

---

## Part E: Pytest Markers and Execution (5 marks)

- Every test is correctly marked smoke, regression, or slow.
- Show that marker selection works, with screenshots of:
```
pytest -m smoke
pytest -m regression
pytest -m slow
```
- No pytest "unknown marker" warnings (the provided `pytest.ini` prevents them
  if you use the three marker names).

---

## Part F: Team Reflection (5 marks)

Answer briefly as a group:
1. Why is running only regression tests before every commit inefficient?
2. Why do smoke tests usually run first in a CI/CD pipeline?
3. What risks arise if slow tests are never run?
4. Can one test belong to two categories? Give an example.
5. Which category do you think gives the most real-world value, and why?

---

## Bonus Challenge (+10 marks)

Write one test that carries TWO markers at once, for example:
```python
@pytest.mark.regression
@pytest.mark.slow
def test_large_order_processing():
    ...
```
Explain why it is a regression test, why it is a slow test, and when it should
run in a CI/CD pipeline. This shows you understand that markers describe
different CHARACTERISTICS of a test, not mutually exclusive boxes.

---

## Marking Rubric (100 + 10)

| Part | Component | Marks |
| --- | --- | --- |
| A | Test type foundations (definitions + examples) | 10 |
| B | Scenario classification with justification | 10 |
| C | Smoke and slow test suite (runnable) | 20 |
| D | Regression bug hunt (find, catch, and fix bugs) | 25 |
| D2 | FINDINGS.md bug-hunt log (how you found them) | 10 |
| D3 | AI usage declaration, comparison, and critique | 15 |
| E | Correct pytest markers and execution evidence | 5 |
| F | Team reflection | 5 |
| | **Total** | **100** |
| Bonus | Multi-marker test with justification | +10 |

Individual contribution is assessed from commit history and test authorship. A
member with no commits and no authored tests may receive a reduced mark.
