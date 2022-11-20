import unittest

from Item import Product
from Checkout import Basket

class CheckoutTest(unittest.TestCase):

    def test_normal_case(p):
        p = Product("A",50,(140,3))
        assert p.calculate_price(7) == 330, "incorrect calculation"

    def test_quantity(mybasket):
        client = [{"code": "A", "quantity": 3}, {"code": "C", "quantity": -1}, {"code": "D", "quantity": 2}]
        mybasket = Basket(client)
        assert mybasket.check_shop(client) == -1, "incorrect checking of quantity"

    def test_total_price(myBasket):
        shop = {}
        shop["A"] = Product("A", 50, (140, 3))
        shop["C"] = Product("C", 25, (None))
        shop["D"] = Product("D", 12, (None))
        client = [{"code": "A", "quantity": 3}, {"code": "C", "quantity": 1}, {"code": "D", "quantity": 2}]
        myBasket = Basket(client)
        myBasket.basket_cost(shop)
        assert myBasket.total_cost == 189, "incorrect calculation of total cost"

    def test_existence(myBasket):
        shop = {}
        shop["A"] = Product("A", 50, (140, 3))
        shop["C"] = Product("C", 25, (None))
        shop["D"] = Product("D", 12, (None))
        client = [{"code": "AA", "quantity": 3}, {"code": "C", "quantity": 1}, {"code": "D", "quantity": 2}]
        myBasket = Basket(client)
        assert myBasket.check_product_existence(client, shop) == -1, "incorrect check for products"

if __name__ == '__main__':
    unittest.main()