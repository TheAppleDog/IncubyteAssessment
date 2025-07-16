#ADD SWEET

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

# DELETE SWEET
def delete_sweet(self, sweet_id):
    self.sweets = [s for s in self.sweets if s.sweet_id != sweet_id]

#  VIEW SWEETS

def view_sweets(self):
    return self.sweets
