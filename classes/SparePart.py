from exceptions.ClassInitializationError import *


class SparePart:

    def __init__(self, name, price):
        if isinstance(name, str) and isinstance(price, int):
            self.__name = name
            self.__price = price
        else:
            raise ClassInitializationError('Name must be string and price must be integer')

    def __repr__(self):
        return f'{self.__name} - {self.__price}$'
