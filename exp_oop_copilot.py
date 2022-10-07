# create Car class with inital values of 'brand' and 'color' and a class to set te price
class Car:
    def __init__(self, brand, color, price=0):
        self.brand = brand
        self.color = color

    def set_price(self, price):
        self.price = price

# method for