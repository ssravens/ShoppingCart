import sys

from Item import Product
from Checkout import Basket


shop = {}
shop["A"] = Product("A",50,(140,3))
shop["B"] = Product("B",35,(60,2))
shop["C"] = Product("C",25, (None))
shop["D"] = Product("D",12, (None))

def user_input():
    choices = {}
    while True:
        code = input("Please enter the code of the product or # to exit:")
        if code == '#':
            break
        if code not in shop:
            print("There is no such code")
            continue
        quantity = int(input("Please enter the quantity of the product:"))
        if quantity <= 0:
            print("Error on quantity")
            continue
        if code in choices:
            tmp_quantity = choices[code]
            tmp_quantity += quantity
            choices[code] = tmp_quantity
        else:
            choices[code] = quantity
    return choices

client = []
choices = user_input()
for key in choices:
    client.append({"code":key,"quantity":choices[key]})
print(client)

mybasket = Basket(client)
mybasket.basket_cost(shop)
print(mybasket.total_cost)