import pytest
from card import ShoppingCart

def test_add_item_negative_price_raises():
    cart = ShoppingCart()
    with pytest.raises(ValueError) as excinfo:
        cart.add_item("apple", -5)
    assert str(excinfo.value) == "Price cannot be negative."

def test_add_item_positive_price():
    cart = ShoppingCart()
    cart.add_item("banana", 2.5, 3)
    assert cart.items == [{"name": "banana", "price": 2.5, "quantity": 3}]
