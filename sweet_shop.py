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

#SEARCH SWEETS BY NAME, CATEGORY OR PRICE RANGE.

def search_by_name(self, name):
    return [s for s in self.sweets if name.lower() in s.name.lower()]

def search_by_category(self, category):
    return [s for s in self.sweets if category.lower() in s.category.lower()]

def search_by_price_range(self, min_price, max_price):
    return [s for s in self.sweets if min_price <= s.price <= max_price]

# SORT SWEETS

def sort_by_price(self):
    return sorted(self.sweets, key=lambda s: s.price)

# PURCHASE SWEETS

def purchase_sweet(self, sweet_id, quantity):
    for s in self.sweets:
        if s.sweet_id == sweet_id:
            if s.quantity >= quantity:
                s.quantity -= quantity
                return
            else:
                raise ValueError("Not enough stock")

# RESTOCKS SWEETS

def restock_sweet(self, sweet_id, quantity):
    for s in self.sweets:
        if s.sweet_id == sweet_id:
            s.quantity += quantity
            return
