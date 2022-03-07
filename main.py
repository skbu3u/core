from classes.Report import *

model_1 = Equipment('HP LaserJet 1020')
part_1 = SparePart('Feed Drive for LaserJet 1020', 10)
model_1.add_part(part_1)
part_2 = SparePart('Repair kit for LaserJet 1020', 30)
model_1.add_part(part_2)

model_2 = Equipment('Cannon 1140')
part_3 = SparePart('Fuser for LaserJet 1020', 50)
part_4 = SparePart('Main Motor for LaserJet 1020', 20)
model_2.add_part_list([part_3, part_4])

model_3 = Equipment('Xerox 2020')
model_3.add_part_list([part_1, part_2, part_3, part_4])

report = Report(model_3)


if __name__ == '__main__':
    print(f'Test add_part method:\n{model_1.dict}\n')
    print(f'Test add_part_list method:\n{model_2.dict}\n')
    print(f'Test report:\n{report.info}\n')
