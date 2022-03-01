from exceptions.ClassInitializationError import *


class SparePart:
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

    def get_all_parts(self):
        if not self.__parts:
            return {'Part name': self.__name}
        else:
            parts_info = {'Part name': self.__name, 'Included parts': []}
            for part in self.__parts:
                parts_info['Included parts'] = [].append(part.get_all_parts())
            return parts_info

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
