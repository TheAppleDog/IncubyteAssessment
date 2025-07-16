# failing test case (red)
# ADD SWEET

import unittest
from sweet_shop import Sweet, SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(sweet)

        self.assertIn(sweet, shop.sweets)

if __name__ == "__main__":
    unittest.main()

# DELETE SWEET

def test_delete_sweet(self):
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    shop.delete_sweet(1001)
    self.assertNotIn(sweet, shop.sweets)

#VIEW SWEETS

def test_view_sweets(self):
    shop = SweetShop()
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gulab Jamun", "Milk-Based", 30, 50)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    result = shop.view_sweets()
    self.assertEqual(len(result), 2)

# SEARCH SWEETS BY NAME, CATEGORY OR PRICE RANGE

def test_search_by_name(self):
    shop = SweetShop()
    shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    result = shop.search_by_name("kaju")
    self.assertEqual(len(result), 1)

def test_search_by_category(self):
    shop = SweetShop()
    shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    shop.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 30))
    result = shop.search_by_category("Milk-Based")
    self.assertEqual(len(result), 1)

def test_search_by_price_range(self):
    shop = SweetShop()
    shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    shop.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 30))
    result = shop.search_by_price_range(5, 30)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0].name, "Gulab Jamun")

# SORT SWEETS

def test_sort_by_price(self):
    shop = SweetShop()
    shop.add_sweet(Sweet(1001, "A", "Candy", 30, 10))
    shop.add_sweet(Sweet(1002, "B", "Candy", 10, 10))
    result = shop.sort_by_price()
    self.assertEqual(result[0].price, 10)

#PURCHASE SWEETS

def test_purchase_sweet_success(self):
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    shop.purchase_sweet(1001, 5)
    self.assertEqual(sweet.quantity, 15)

# NOT ENOUGH STOCK

def test_purchase_sweet_insufficient_stock(self):
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 3)
    shop.add_sweet(sweet)
    with self.assertRaises(ValueError):
        shop.purchase_sweet(1001, 5)

# RESTOCK SWEETS

def test_restock_sweet(self):
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 5)
    shop.add_sweet(sweet)
    shop.restock_sweet(1001, 10)
    self.assertEqual(sweet.quantity, 15)
