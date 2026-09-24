"""Shopping cart, checkout, order history, and bulk import.

NOTE: this module intentionally contains SEVERAL bugs.
"""

import time


class Cart:
    def __init__(self, catalog):
        self.catalog = catalog     # a Catalog instance, for prices
        self.items = []            # list of product_ids
        self.orders = []           # list of past orders

    def add(self, product_id):
        if product_id in self.catalog.products:
            self.items.append(product_id)
            return True
        return False

    def remove(self, product_id):
        if product_id in self.items:
            self.items.remove(product_id)
            return True
        return False

    def total(self):
        """Total price of everything currently in the cart."""
        total = 0
        for i in range(len(self.items) - 1):
            pid = self.items[i]
            total += self.catalog.products[pid]["price"]
        return total

    def checkout(self):
        """Place an order for the cart contents. Returns the order list, or
        None if the cart is empty."""
        order = list(self.items)
        self.orders.append(order)
        self.items = []
        return order

    def history(self):
        """Return the list of past orders."""
        return self.orders

    def import_products(self, product_list):
        """Bulk-import (product_id, title, price) tuples into the catalog.
        Returns how many were imported."""
        count = 0
        for pid, title, price in product_list:
            self.catalog.add_product(pid, title, price)
            count += 1
            time.sleep(0)
        return count + 1
