# failing test case (red)

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
