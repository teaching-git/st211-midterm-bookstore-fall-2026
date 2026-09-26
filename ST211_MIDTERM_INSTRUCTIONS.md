# Midterm Project: Testing an Online Bookstore with Pytest

## Automated Software Testing (192-211)

### Overview

Your team is the Quality Assurance team for a new online bookstore. You are
given the application code — and it contains bugs. Your job is to design a
testing strategy using smoke, regression and slow tests, implement it with
pytest markers, and above all **write tests that catch the bugs**.

Group project (3–5 students). **100 marks**, plus a 10-mark bonus.


---

## How Your Tests Are Graded (Read This First)

Fifty-five of the 100 marks for this project come from running your code, not from inspecting it. Understanding how the grading works will help you approach the project correctly.

### Regression Tests

**Regression tests are run against the original, unfixed application.**

After submission, your `tests/` directory will be copied into a fresh copy of the starter code, and `pytest` will be executed.

Every test marked with `@pytest.mark.regression` **must fail** against the original buggy application. If a regression test passes on the original code, it has not demonstrated that it can detect the bug and will receive **zero marks**, regardless of how well the test is written.

For this reason, you should:

1. Write the test first.
2. Verify that it fails on the original application.
3. Only then implement the fix.

A regression test written after the bug has already been fixed may appear correct in your repository, but there is no evidence that it ever detected the original defect.

### Bug Fixes

**Your fixes are evaluated using a hidden acceptance test suite.**

Making your own test pass does not prove that the fix is correct. A poorly implemented change can satisfy a specific test while breaking the intended behaviour.

After your regression tests are assessed, a hidden acceptance suite is run against your fixed application. That suite defines the expected behaviour and determines whether your fixes are correct.

### Smoke Tests

**Smoke tests are run against deliberately broken versions of the application.**

Five faulty variants are used during grading. In each variant, one major feature has been intentionally broken:

- User registration always fails.
- Login accepts any password.
- Products are not saved.
- Items never reach the cart.
- Checkout produces no result.

Your Part C mark depends on how many of these failures your smoke suite detects. A smoke suite that does not meaningfully exercise the application's core functionality will receive little or no credit.

### Important Distinction: Smoke vs Regression Tests

Smoke tests verify that key features work at a basic level and therefore **must pass on the original application provided to you**.

If a supposed smoke test fails on the original code, then it has identified a defect rather than verified basic functionality. In that case, it belongs in the regression suite and should be marked as a regression test.

A useful rule of thumb is:

> **Smoke tests should pass on the original application and fail on deliberately broken variants.**
>
> **Regression tests should fail on the original application and pass after the bug is fixed.**

---

## Getting the code

You start from the template repository:
**https://github.com/teaching-git/st211-midterm-bookstore-fall-2026.git**

**Do not push your work to my repository.** Make your own copy, work there, and
submit your copy's link.

### Easiest way: "Use this template"

1. Open the repository link on GitHub.
2. Click the green **Use this template** button → **Create a new repository**.
3. Name it `st211-midterm-<your-group-name>` and set it to **Private**.
4. Add me as a collaborator (Settings → Collaborators).
5. Clone **your** new repository and start working.

### Alternative: clone and re-push

```
git clone https://github.com/teaching-git/st211-midterm-bookstore-fall-2026.git st211-midterm-<group>
cd st211-midterm-<group>
rm -rf .git
git init && git add . && git commit -m "start midterm"
```

Then create an empty private repository on your own account and push to it.

### What is in the repository

```
bookstore_app/        the application (assume nothing is correct)
  users.py              registration and login
  catalog.py            products and search
  cart.py               cart, checkout, orders, bulk import
tests/
  test_bookstore.py     where your tests go
worked_example/       a fully worked bug, start, here
  notes.py              a small module with one bug in it
  test_notes.py         the failing test that catches it
  WALKTHROUGH.md        how it was found, written up the way yours should be
ai_review/            the AI-generated test set you must audit in Part D3
templates/            FINDINGS.md, AI_USAGE.md, REPORT.md to copy and fill in
.github/workflows/    a starter CI workflow for Part E
pytest.ini            registers the three markers
README.md
```

Set up and confirm it runs:

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

**Start with `worked_example/`.** It contains one bug, the test that catches it,
and a short walkthrough of how it was found — written in the format your own
findings should use. It is not graded. It exists so you know what "done" looks
like before you begin.

---

## What to submit

1. Your test suite in `tests/`, committed progressively.
2. `REPORT.md` — covering Parts A/B and F.
3. `FINDINGS.md` — your bug-hunt log (Part D2).
4. `AI_USAGE.md` — your AI declaration and the Part D3 audit.
5. Your group's repository URL.

**Work progressively.** Small commits from several people, with clear messages.
A single "upload" commit at the end from one person is a red flag, and the
commit history is part of how individual contribution is assessed.

**Name every test's author** in its docstring:

```python
def test_cart_total_includes_last_item():
    """Author: Mai. Regression test for the cart total bug."""
```

Authorship claims are cross-checked against `git blame`.

---

## Part A/B — Test types and classification (10 marks)

**A.** For each of smoke, regression and slow testing: define it in your own
words, say when it should run, and give two examples relevant to this bookstore.

**B.** For each scenario below, say whether it is smoke, regression or slow (it
may be more than one) and justify in two or three sentences. These describe a
generic e-commerce system, not necessarily this one.

1. Verify that a password-reset email is delivered within one minute.
2. Verify that a previously fixed bug in shipping-cost calculation has not
   returned.
3. Verify that a nightly job can generate a sales report from ten years of
   orders.
4. Verify that the payment page loads after every deployment.
5. Verify that a refund issued twice does not credit the customer twice — a
   fault reported by a customer last quarter.
6. Verify that the recommendation engine still responds when the catalogue
   holds one million titles.

Both parts go in `REPORT.md`. Keep it tight; marks are for the justification,
not the word count.

---

## Part C — Smoke and slow test suite (25 marks)

Write real, runnable tests in `tests/test_bookstore.py`.

**Smoke tests — at least five.** Quick checks that core features work at all:
register a new user, log in, add a product, add to cart, check out with a
non-empty cart. Mark each `@pytest.mark.smoke`. They must pass against the code
as shipped.

**Slow tests — at least two.** Exercise the application with large data:
importing tens of thousands of products, or many operations in a loop. Mark each
`@pytest.mark.slow` and explain in a comment what makes it slow.

Marking:

- **20 marks** — how many of my five broken variants your smoke suite detects
  (4 marks each). Write smoke tests that would actually notice if the feature
  stopped working.
- **5 marks** — the slow tests run, do meaningful work, and are measurably
  slower than the smoke suite. `pytest -m smoke` should finish in a couple of
  seconds; each slow test should take noticeably longer. A test marked slow that
  runs instantly is mislabelled.

---

## Part D — The bug hunt (30 marks)

The application contains **exactly six planted bugs**, spread across
`users.py`, `catalog.py` and `cart.py`. They sit on a deliberate difficulty
ladder: **two are straightforward**, **two take some thought**, and **two are
subtle** — the kind that pass a casual read and only show up when you exercise
the code carefully.

You are not told what they are. Find them by reading each module, deciding what
each function is *supposed* to do, and writing a test that checks it.

For each bug you find, write a regression test that:

- **FAILS** against the application as shipped — this is what proves your test
  detects something real; then
- **PASSES** after you fix the bug in `bookstore_app/`.

Mark each `@pytest.mark.regression`. In the docstring, name the function,
describe the wrong behaviour you observed, and state what the correct behaviour
is.

**Marking — 5 marks per bug, six bugs, 30 marks:**

| | marks |
|---|---|
| A regression test that genuinely fails against the shipped code | 3 |
| A correct fix, confirmed by the hidden acceptance suite | 2 |

You do not have to find all six to score well. Four found and properly handled
is a solid result. Finding the two subtle ones is what separates the top groups.

**A warning that is worth 3 marks per bug:** if you fix the application first
and write the test afterwards, your test will pass against the buggy code in my
run, and you will lose the detection marks for that bug even though the bug is
genuinely fixed. Test first. Commit the failing test *before* you commit the fix
— that also gives you an honest history to point at.

---

## Part D2 — Bug-hunt log, FINDINGS.md (5 marks)

One entry per bug, **five entries maximum**, about 150 words each. Use the
template. For each:

- **Suspected** — which function, and what made you suspicious.
- **Tried** — the input or the test you used to check.
- **Observed** — the actual, wrong result. Paste it.
- **Expected** — the correct behaviour, and why you believe that is correct.
- **Fixed** — what you changed.

Marks are for the **observed / expected pair being specific and checkable**. "It
did not work properly" earns nothing; "`cart_total([a,b,c])` returned 24.50, the
sum of the first two items only; it should return 37.00" earns full marks. Write
it as you go — an entry written from memory a week later shows.

---

## Part D3 — AI Declaration and Test Audit (20 marks)

Modern software testers use AI-assisted tools. This part assesses your ability to use those tools **critically**, rather than accepting their output without verification.

### D3.1 — AI Declaration (Required)

In `AI_USAGE.md`, declare **every AI tool** used by your group during this project and briefly describe how it was used.

Using AI is permitted. Declaring its use is mandatory.

For each tool, include:

- The tool name (e.g., ChatGPT, Copilot, Claude, Gemini).
- What it was used for.
- Whether its output was accepted directly, modified, or rejected.

Failure to declare AI usage that is discovered during grading may be treated as an academic-integrity matter.

Example:

```text
Tool: ChatGPT
Purpose: Generated candidate regression tests and suggested bug-fix strategies.
Outcome: All generated code was reviewed, modified, and validated manually before use.
```

### D3.2 — Audit the Supplied Test Set (16 marks)

The `ai_review/` directory contains a set of tests for the bookstore application that were generated by an AI assistant and presented as a completed bug-hunt.

The tests are intentionally mixed in quality.

Some tests genuinely detect a planted bug.

Some appear reasonable but **pass against the buggy application**, meaning they do not detect anything.

Some assert behaviour that the application was never intended to provide and therefore represent an **invented bug** rather than a real defect.

For **each** test in `ai_review/`, record your findings in `AI_USAGE.md` using the following format:

| Test | Claimed Bug | Does It Actually Detect It? | Evidence | Verdict |
|---|---|---|---|---|
| `test_...` | Description of the claimed bug | Yes / No | Command and actual output | Genuine bug / Passes anyway / Invented bug |

For every test:

1. Run the test against the original supplied application.
2. Record the command used.
3. Paste the relevant output.
4. Explain what the output demonstrates.
5. Assign a final verdict.

#### Evidence Matters

The evidence is the graded component of this task.

A correct verdict without supporting output will receive only partial credit.

A verdict must be justified by the actual behaviour observed when the test is executed.

Typical commands include:

```bash
pytest ai_review/test_example.py -v
```

or

```bash
pytest ai_review/test_example.py -q
```

Your conclusion should be based on the observed result, not on what the test appears to be checking.

### D3.3 — Reflection and Final Verdict (4 marks)

Write a short reflective discussion addressing the following questions:

1. Which failure mode was most common in the supplied AI-generated test set?
2. Why is a test that passes against buggy code potentially more dangerous than a test that crashes?
3. What lessons did you learn from auditing AI-generated tests?
4. What checks will you perform in future before trusting a generated test?

A strong reflection should focus on evidence

---

## Part E — Markers and continuous integration (5 marks)

A starter workflow is in `.github/workflows/`. Complete it so that on your
repository:

- every push runs `pytest -m smoke`;
- a scheduled nightly run executes the full suite including slow tests;
- the run is green at submission time.

Marks are for a workflow that actually runs on GitHub Actions — I will look at
your Actions tab, not at a screenshot. All tests must carry exactly one of the
three markers, with no "unknown marker" warnings.

---

## Part F — Team reflection (5 marks)

Briefly, as a group, in `REPORT.md`:

1. Why is running only regression tests before every commit inefficient?
2. Why do smoke tests usually run first in a CI/CD pipeline?
3. What risks arise if slow tests are never run?
4. Can one test belong to two categories? Give an example.
5. In this project you both found the bugs and fixed them. In a real QA team
   those are often different people. What does that separation change about how
   a bug report has to be written?

---

## Bonus challenge (+10 marks)

Write one test carrying two markers at once:

```python
@pytest.mark.regression
@pytest.mark.slow
def test_large_order_processing():
    ...
```

Explain why it is a regression test, why it is slow, and where it belongs in a
CI/CD pipeline. Markers describe different *characteristics* of a test, not
mutually exclusive boxes. The bonus can take a group above 100.

---

## Marking rubric

| Part | Component | Marks |
|---|---|---|
| A/B | Test types and scenario classification | 10 | 
| C | Smoke and slow suite — 5 variants × 4, plus 5 for slow tests | 25 | 
| D | Bug hunt — 6 bugs × (3 detect + 2 fix) | 30 |
| D2 | FINDINGS.md bug-hunt log | 5 |
| D3 | AI declaration and audit of the supplied test set | 20 |
| E | Markers and a working CI workflow | 5 | Actions log |
| F | Team reflection | 5 |
| | **Total** | **100** |
| Bonus | Multi-marker test with justification | +10 |

Individual contribution within the group is assessed from commit history and
from test authorship cross-checked against `git blame`. A member with no
commits and no authored tests may receive a reduced mark.

