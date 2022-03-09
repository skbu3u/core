from exceptions.ClassInitializationError import ClassInitializationError


class SparePart:

    def __init__(self, name, price):
        self.__parts = {}
        self.__included_parts = []
        if isinstance(name, str) and isinstance(price, int):
            self.__name = name
            self.__price = price
        else:
            raise ClassInitializationError('Name must be string and price must be integer')

    def __repr__(self):
        return "{'%s': {'Price': %s, 'Included_parts': []}}" % (self.__name, self.__price)

    def add_part(self, part):
        if isinstance(part, SparePart):
            self.__included_parts.append(part)
            self.__parts = {self.__name: {'Price': self.__price, 'Included_parts': self.__included_parts}}
        else:
            raise ClassInitializationError('Part must be SparePart class')

    def add_part_list(self, part_list):
        if isinstance(part_list, list):
            for part in part_list:
                self.add_part(part)
        else:
            raise ClassInitializationError('Parts must be array of SparePart')

    @property
    def get_parts(self):
        return self.__parts
