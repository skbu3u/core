from classes.SparePart import *
from exceptions.ClassInitializationError import *


class Equipment:

    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ClassInitializationError('Name must be string')
        self.__dict = {}

    def add_part(self, part):
        if isinstance(part, SparePart):
            self.__dict.setdefault(self.__name, []).append(part)
        else:
            raise ClassInitializationError('Part must be SparePart class')

    def add_part_list(self, part_list):
        if not isinstance(part_list, list):
            raise ClassInitializationError('Parts must be array of SparePart')
        else:
            for part in part_list:
                if isinstance(part, SparePart):
                    self.__dict.setdefault(self.__name, []).append(part)
                else:
                    raise ClassInitializationError('Part must be SparePart class')

    def extract_part(self, part):
        if self.__dict[part]:
            self.__dict.setdefault(part).pop(0)

    @property
    def dict(self):
        return self.__dict
