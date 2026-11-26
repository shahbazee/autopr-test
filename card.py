class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        # Reject negative prices
        if price < 0:
            raise ValueError("Price cannot be negative.")
        for item in self.items:
            if item["name"] == name:
                item["quantity"] += quantity
                return
        self.items.append(
            {"name": name, "price": price, "quantity": quantity}
        )

    def remove_item(self, name):
        self.items = [
            item for item in self.items if item["name"] != name
        ]

    def total(self):
        amount = 0
        for item in self.items:
            amount += item["price"]
        return amount

    def apply_discount(self, percent):
        amount = self.total()
        discount = amount * percent / 100
        return amount - discount

    def item_count(self):
        count = 0
        for item in self.items:
            count += item["quantity"]
        return count

    def clear(self):
        self.items = []
