import pytest
from card import ShoppingCart

def test_total_single_item_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 3)
    assert cart.total() == 6

def test_total_multiple_items_and_quantities():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 3)      # 6
    cart.add_item("banana", 1.5, 2)   # 3
    cart.add_item("orange", 4)        # 4 (default quantity 1)
    assert cart.total() == pytest.approx(13)

def test_total_accumulates_when_adding_same_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 1)
    cart.add_item("apple", 2, 2)  # quantity should become 3
    assert cart.item_count() == 3
    assert cart.total() == 6
