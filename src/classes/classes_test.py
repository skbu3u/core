from src.classes.SparePart import SparePart
from src.classes.Equipment import Equipment
from src.classes.Report import Report

part_1 = SparePart('Картридж', 10)
part_1_1 = SparePart('Тонер', 3)
part_1_2 = SparePart('Вал', 5)
part_1_3 = SparePart('Ракель', 2)
part_2 = SparePart('Печь', 40)
part_3 = SparePart('Плата', 70)

part_1.add_part(part_1_1)
part_1.add_part_list([part_1_2, part_1_3])

model = Equipment('Принтер')

model.add_part(part_1)
model.add_part_list([part_2, part_3])

report = Report(model)

print(report.info)
