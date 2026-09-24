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
`<INSTRUCTOR_REPO_URL>` (your instructor will give you the exact link).

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
git clone <INSTRUCTOR_REPO_URL> st211-midterm-<group>
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
2. A Test Design Report (PDF) covering Parts A, B, and F below.
3. Your group's repository URL.

**Work progressively.** Commit as you go, with clear messages. A history of
small commits from several people is expected. A single "upload" commit at the
end from one person is a red flag.

**Name every test's author.** Each test's docstring must say who wrote it, e.g.
`"""Author: Mai. Regression test for the cart-total bug."""` This is how
individual contribution is graded.

---

## Part A: Test Type Foundations (15 marks)

For each of smoke, regression, and slow testing:
- Define it in your own words.
- Explain when it should be run.
- Give 3 examples relevant to this bookstore.

---

## Part B: Classification Challenge (15 marks)

For each scenario, state whether it is a smoke, regression, or slow test (or
more than one), and justify in 2-3 sentences.

1. Verify that users can log in successfully.
2. Verify that a previously fixed discount-calculation bug does not reappear.
3. Verify importing 100,000 products.
4. Verify that checkout works after each deployment.
5. Verify that a bug involving special characters in passwords remains fixed.
6. Verify generating annual sales reports from 10 years of data.

---

## Part C: Smoke and Slow Test Suite (25 marks)

Write REAL, RUNNABLE tests in `tests/test_bookstore.py`.

**Smoke tests (at least 5):** quick checks that core features work at all --
register, login (with a valid simple password), add a product, add to cart,
checkout with a non-empty cart. Mark each `@pytest.mark.smoke`.

**Slow tests (at least 2):** exercise the app with large data, for example
importing tens of thousands of products, or performing many operations in a
loop. Mark each `@pytest.mark.slow`. In a comment, explain what makes it slow.

Marks are for tests that actually run and genuinely check the feature.

---

## Part D: The Bug Hunt -- Regression Tests (30 marks)

The application contains **6 bugs**. Three are described below. **Three more are
undocumented** -- you must find them by exploring the code and testing its
behaviour.

For EACH bug you catch, write a regression test that:
- FAILS while the bug is present (this proves your test detects it), then
- PASSES after you fix the bug in `bookstore_app/`.

Mark each `@pytest.mark.regression`, and in the docstring describe the bug.

**Bugs are hidden** in the code. Look carefully at search, order
history, and bulk import. Finding and catching them is where the strongest
groups distinguish themselves.

Marking (per bug, up to 6 bugs):
- Regression test that correctly fails against the buggy code: 3 marks.
- Correct fix so the test then passes: 2 marks.


---

## Part E: Pytest Markers and Execution (10 marks)

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
| A | Test type foundations (definitions + examples) | 15 |
| B | Scenario classification with justification | 15 |
| C | Smoke and slow test suite (runnable) | 25 |
| D | Regression bug hunt (tests that catch + fix bugs) | 30 |
| E | Correct pytest markers and execution evidence | 10 |
| F | Team reflection | 5 |
| | **Total** | **100** |
| Bonus | Multi-marker test with justification | +10 |

Individual contribution is assessed from commit history and test authorship. A
member with no commits and no authored tests may receive a reduced mark.
