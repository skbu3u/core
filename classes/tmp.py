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


class SparePart:

    def __init__(self, name, price):
        if isinstance(name, str) and isinstance(price, int):
            self.__name = name
            self.__price = price
        else:
            raise ClassInitializationError('Name must be string and price must be integer')

    def __repr__(self):
        return f'{self.__name} - {self.__price}$'


model_1 = Equipment('HP LaserJet 1020')
part_1 = SparePart('Feed Drive for LaserJet 1020', 10)
model_1.add_part(part_1)
part_2 = SparePart('Repair kit for LaserJet 1020', 30)
model_1.add_part(part_2)

model_2 = Equipment('Cannon 1140')
part_3 = SparePart('Fuser for LaserJet 1020', 50)
model_2.add_part(part_3)
part_4 = SparePart('Main Motor for LaserJet 1020', 20)
model_2.add_part(part_4)

model_3 = Equipment('Xerox 2020')
model_3.add_part_list([part_1, part_2, part_3, part_4])

print(model_1.dict)
print(model_2.dict)
print(model_3.dict)