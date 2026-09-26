"""AI-generated test set for the bookstore (for your Part D3 audit).

This set was produced by an AI assistant and presented as a finished bug hunt.
It looks competent. It is not all correct. For EACH test below, determine
whether it genuinely catches a planted bug, passes against the buggy code (so
detects nothing), or asserts behaviour the application was never meant to have.
Run each one and paste the evidence in AI_USAGE.md.
"""
from bookstore_app import Users, Catalog, Cart


def test_cart_total_sums_items():
    """Claims to check the cart total is correct."""
    cat = Catalog(); cat.add_product(1, "A", 10); cat.add_product(2, "B", 20)
    c = Cart(cat); c.add(1); c.add(2)
    assert c.total() == 30


def test_login_rejects_wrong_password():
    """Claims to check that a wrong password is rejected."""
    u = Users(); u.register("alice", "secret1")
    assert u.login("alice", "wrongpw") is False


def test_search_finds_exact_title():
    """Claims to check that search finds a product."""
    cat = Catalog(); cat.add_product(1, "Python Testing", 30)
    assert cat.search("Python Testing") == [1]


def test_import_returns_count():
    """Claims to check the bulk-import count."""
    c = Cart(Catalog())
    assert c.import_products([(1, "A", 5), (2, "B", 6)]) == 2


def test_register_duplicate_returns_false():
    """Claims to check that duplicate registration fails."""
    u = Users(); u.register("bob", "pw")
    assert u.register("bob", "pw") is False


def test_checkout_empty_returns_none():
    """Claims to check that checking out an empty cart returns None."""
    assert Cart(Catalog()).checkout() is None


def test_add_to_cart_returns_true_for_known_product():
    """Claims to check adding a known product to the cart."""
    cat = Catalog(); cat.add_product(1, "A", 10)
    c = Cart(cat)
    assert c.add(1) is True


def test_search_is_limited_to_ten_results():
    """Claims the catalogue search returns at most ten results."""
    cat = Catalog()
    for i in range(20):
        cat.add_product(i, "match", 1)
    assert len(cat.search("match")) <= 10
