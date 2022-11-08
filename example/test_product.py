
import unittest
from example.cart import ShoppingCart
from example.product import Product

class ShoppingCartTestCase(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    
    def test_cart_initially_empty(self):
        self.cart = ShoppingCart()
        self.assertDictEqual({}, {}) 


    def test_add_and_remove_product(self):
        self.cart = ShoppingCart()
        product = Product('Polo', 'S', 'Navy Blue')
        
        self.cart.add_product(product)
        self.cart.remove_product(product)
        # Check if the products attribute is empty
        # The assertDictEqual check if two dicts are equal
        self.assertDictEqual({}, self.cart.products) 
    
    



unittest.main(argv=[''], verbosity=3, exit=False)



