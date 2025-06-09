import unittest
from shopping_cart import calculate_total

class TestShoppingCart(unittest.TestCase):

    def test_total_empty_cart(self):
        self.assertEqual(calculate_total([]), 0)

    def test_total_single_item(self):
        cart = [{'name': 'apple', 'price': 1.0}]
        self.assertEqual(calculate_total(cart), 1.0)

    def test_total_multiple_items(self):
        cart = [
            {'name': 'apple', 'price': 1.0},
            {'name': 'banana', 'price': 2.0}
        ]
        self.assertEqual(calculate_total(cart), 3.0)

if __name__ == '__main__':
    unittest.main()
