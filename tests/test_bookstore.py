"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry exactly one marker (@pytest.mark.smoke / regression /
slow) and name its author in the docstring, e.g.:

    @pytest.mark.smoke
    def test_login_works():
        '''Author: <name>. Smoke test for login.'''

Run:  pytest            (all)     pytest -m smoke     pytest -m regression
"""
import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke: a new user can register."""
    assert Users().register("newuser", "password123") is True


# ---- YOUR SMOKE TESTS (at least 5) ----

# ---- YOUR REGRESSION TESTS (the bug hunt) ----

# ---- YOUR SLOW TESTS (at least 2) ----


# ---- REGRESSION TESTS ----

@pytest.mark.regression
def test_login_preserves_special_characters():
    """Author: Your Name. Regression: login must compare the exact password."""
    users = Users()
    users.register("alice", "p@ss!123")

    assert users.login("alice", "p@ss!123") is True


@pytest.mark.regression
def test_cart_total_includes_last_item():
    """Author: Your Name. Regression: total must include every cart item."""
    catalog = Catalog()
    catalog.add_product("A", "Book A", 100)
    catalog.add_product("B", "Book B", 200)
    catalog.add_product("C", "Book C", 300)

    cart = Cart(catalog)
    cart.add("A")
    cart.add("B")
    cart.add("C")

    assert cart.total() == 600


@pytest.mark.regression
def test_checkout_empty_cart_returns_none():
    """Author: Your Name. Regression: empty cart must not create an order."""
    catalog = Catalog()
    cart = Cart(catalog)

    assert cart.checkout() is None
    assert cart.orders == []


@pytest.mark.regression
def test_import_products_returns_correct_count():
    """Author: Your Name. Regression: import must return the actual count."""
    catalog = Catalog()
    cart = Cart(catalog)

    products = [
        ("A", "Book A", 100),
        ("B", "Book B", 200),
        ("C", "Book C", 300)
    ]

    assert cart.import_products(products) == 3
