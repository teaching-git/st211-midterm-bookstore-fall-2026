"""Product catalog: adding products and searching.

NOTE: this module intentionally contains at least one bug.
"""


class Catalog:
    def __init__(self):
        self.products = {}   # product_id -> {"title":..., "price":...}

    def add_product(self, product_id, title, price):
        self.products[product_id] = {"title": title, "price": price}

    def search(self, keyword):
        """Return a list of product_ids whose title contains the keyword."""
        results = []
        for pid, info in self.products.items():
            if keyword in info["title"]:
                results.append(pid)
        return results
