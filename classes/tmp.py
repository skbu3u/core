from exceptions.ClassInitializationError import *


class Report:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name}-{self.price}'


class SparePart(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)


report = Report()
# создаем объект и добавляем
part_1 = SparePart('hp', '321')
report.add_to(part_1)
part_2 = SparePart('canon', '1211')
report.add_to(part_2)

# выводим склад
print(report._dict)
