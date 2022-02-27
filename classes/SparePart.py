from exceptions.ClassInitializationError import *


class SparePart:
    __parts = []
    __name = ''

    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
            # self.__parts.append(name)
        else:
            raise ClassInitializationError('Name must be string')

    def get_parts_info(self):
        parts = self.__parts
        return parts

    def add_part(self, parts):
        if isinstance(parts, list):
            self.__parts += parts
        else:
            raise ClassInitializationError('Parts must be array of SparePart')
