class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.sweet_id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} ({self.category}) - ₹{self.price} x {self.quantity}"

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)
