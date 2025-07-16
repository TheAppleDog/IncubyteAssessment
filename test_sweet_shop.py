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
