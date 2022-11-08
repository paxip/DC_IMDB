
import unittest
from example.cart import ShoppingCart
from example.product import Product

class ShoppingCartTestCase(unittest.TestCase):
    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('Polo', 'S', 'Navy Blue')
        
        cart.add_product(product)
        cart.remove_product(product)
        # Check if the products attribute is empty
        # The assertDictEqual check if two dicts are equal
        self.assertDictEqual({}, cart.products) 

unittest.main(argv=[''], verbosity=3, exit=False)



