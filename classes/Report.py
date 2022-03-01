from classes.Equipment import *
from classes.SparePart import *


class Report(Equipment):

    def __init__(self, name, price):
        Equipment.__init__(self, name)
        self.price = price

    def info(self):
        pass


report = Report('HP LaserJet 1020', 200)
model = Equipment('HP LaserJet 1020')
part_1 = SparePart('Feed Drive for LaserJet 1020')
part_2 = SparePart('Repair kit for LaserJet 1020')
part_3 = SparePart('Fuser for LaserJet 1020')
part_4 = SparePart('Main Motor for LaserJet 1020')
model.add_part([part_1, part_2, part_3, part_4])

print(model.info())
