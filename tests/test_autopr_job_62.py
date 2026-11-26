import pytest
from card import ShoppingCart

def test_get_most_expensive_item_basic():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    cart.add_item("banana", 5)
    assert cart.get_most_expensive_item() == "banana"

def test_get_most_expensive_item_empty():
    cart = ShoppingCart()
    assert cart.get_most_expensive_item() is None

def test_get_most_expensive_item_tie():
    cart = ShoppingCart()
    cart.add_item("apple", 5)
    cart.add_item("banana", 5)
    assert cart.get_most_expensive_item() in ("apple", "banana")

def test_get_most_expensive_item_quantity_update():
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    cart.add_item("apple", 3, quantity=2)  # updates quantity, price unchanged
    cart.add_item("banana", 4)
    assert cart.get_most_expensive_item() == "banana"
