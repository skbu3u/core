from src.classes.SparePart import SparePart
from src.exceptions.ClassInitializationError import ClassInitializationError


class Equipment:

    def __init__(self, name):
        self.__parts = {}
        self.__included_parts = []
        if isinstance(name, str):
            self.__name = name
        else:
            raise ClassInitializationError('Name must be string and price must be integer')

    def add_part(self, part):
        if isinstance(part, SparePart):
            if part.get_parts:
                self.__included_parts.append(part.get_parts)
            else:
                self.__included_parts.append(part)
            self.__parts = {self.__name: {'Included_parts': self.__included_parts}}
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
