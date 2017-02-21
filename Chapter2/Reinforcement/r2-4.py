# Write a Python class, Flower, that has 3 instance variables of type str, int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type.

class Flower:

    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    @property
    def name(self):
        return self.name

    @property 
    def petals(self):
        return self.petals

    @property
    def price(self):
        return self.price

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @petals.setter
    def petals(self, new_petals):
        self.petals = new_petals

    @price.setter
    def price(self, new_price):
        self.price = price


