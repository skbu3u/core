from exceptions.ClassInitializationError import *


class Equipment:
    def __init__(self, name):
        self.name = name
        self._dict = {}

    def add_to(self, part):
        self._dict.setdefault(self.name, []).append(part)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class SparePart:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name} - {self.price}$'


model_1 = Equipment('HP LaserJet 1020')

part_1 = SparePart('Feed Drive for LaserJet 1020', 10)
model_1.add_to(part_1)
part_2 = SparePart('Repair kit for LaserJet 1020', 30)
model_1.add_to(part_2)

model_2 = Equipment('Cannon 1140')

part_3 = SparePart('Fuser for LaserJet 1020', 50)
model_2.add_to(part_3)
part_4 = SparePart('Main Motor for LaserJet 1020', 20)
model_2.add_to(part_4)

print(model_1.dict)
print(model_2.dict)
