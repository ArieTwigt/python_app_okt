from typing import Union

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def define_price(self, price: Union[int, float]):
        self.price = price

    def __repr__(self) -> str:

        return f"{self.brand} - {self.model}"
