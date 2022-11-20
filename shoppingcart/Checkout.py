from Item import Product

class Basket:

    def __init__(self,products):
        self.product_list = products #[{"code":A, "quantity:3}, {....}]
        self.total_cost = 0

    def check_shop(self,products):
        for product in products:
            if product["quantity"] <= 0:
                return -1

    def check_product_existence(self,products,shop):
        for product in products:
            code = product["code"]
            if code not in shop:
                return -1

    def basket_cost(self,shop):
        self.total_cost = 0
        for product in self.product_list:
            code = product["code"]
            quantity = product["quantity"]
            selected_product = shop[code]
            product_cost = selected_product.calculate_price(quantity)
            self.total_cost += product_cost





