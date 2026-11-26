import pytest
from card import ShoppingCart

def test_total_multiplies_price_by_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 3)  # 3 apples at $2 each should be $6
    assert cart.total() == 6

def test_total_with_multiple_items():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 3)   # $6
    cart.add_item("banana", 1, 5)  # $5
    assert cart.total() == 11
    # Adding more of an existing item should update quantity and total accordingly
    cart.add_item("apple", 2, 2)   # now 5 apples total -> $10, plus $5 bananas = $15
    assert cart.total() == 15
    # Ensure item count reflects total quantity
    assert cart.item_count() == 5 + 5  # 5 apples + 5 bananas = 10
