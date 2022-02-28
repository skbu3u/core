from classes.SparePart import *
from exceptions.ClassInitializationError import *


class Equipment:
    __parts = []
    __name = ''

    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ClassInitializationError('Name must be string')

    def get_parts(self):
        parts = self.__parts
        return parts

    def add_part(self, parts):
        if not isinstance(parts, list):
            raise ClassInitializationError('Parts must be array of SparePart')
        else:
            for part in parts:
                if isinstance(part, SparePart):
                    pass
                else:
                    raise ClassInitializationError('Part must be SparePart class')
            self.__parts += parts
