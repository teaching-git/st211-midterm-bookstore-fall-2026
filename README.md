# Bookstore QA Midterm

A small (buggy!) online-bookstore app for you to test.

## Layout
```
bookstore_app/      the application (DO NOT assume it is correct)
  users.py          registration + login
  catalog.py        products + search
  cart.py           cart, checkout, orders, bulk import
tests/
  test_bookstore.py YOUR test suite goes here
pytest.ini          registers the smoke/regression/slow markers
```

## Setup
```
pip install pytest
```

## Running tests
```
pytest                 # everything
pytest -m smoke        # only smoke tests
pytest -m regression   # only regression tests
pytest -m slow         # only slow tests
```

See the assignment instructions (PDF) for what to build and how it is graded.
# st211-midterm-bookstore-fall-2026
