class Product:

    def __init__(self,code,price,special_price=None):
        self.code = code
        self.price = price
        self.special_price = special_price

    def calculate_price(self, quantity):
        if self.special_price is None:
            return self.price * quantity
        # special price but the desired quantity less than the threshold of special price
        if quantity < self.special_price[1]:
            return self.price * quantity
        # any other case that exploits the special price
        discount_items = quantity // self.special_price[1]
        normal_price_items = quantity % self.special_price[1]
        return self.price * normal_price_items + self.special_price[0] * discount_items