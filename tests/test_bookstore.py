"""
Bookstore QA Midterm -- your test suite goes here.

Import the app modules and write your tests below. Use pytest markers to
categorize every test:  @pytest.mark.smoke / regression / slow

Every test must name its author in the docstring, e.g.:
    def test_login_works():
        '''Author: <your name>. Smoke test for login.'''

Run your tests with:
    pytest                 # all tests
    pytest -m smoke        # only smoke tests
    pytest -m regression   # only regression tests
    pytest -m slow         # only slow tests
"""
import pytest
from bookstore_app import Users, Catalog, Cart


# ---------------- EXAMPLE (delete or keep) ----------------
@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke test: a new user can register."""
    users = Users()
    assert users.register("newuser", "password123") is True


# ---------------- YOUR SMOKE TESTS ----------------
# TODO: add at least 5 smoke tests for the working features.


# ---------------- YOUR REGRESSION TESTS (the bug hunt) ----------------
# TODO: write tests that CATCH the bugs. A good regression test FAILS while
# the bug is present, and PASSES once the bug is fixed.


# ---------------- YOUR SLOW TESTS ----------------
# TODO: add slow tests (e.g. importing a very large product list).
