class Equipment:
    name = 'Equipment'
    printer = False
    scaner = False
    xerox = False

    def info(self):
        print(f'Name: {self.name}\n'
              f'Printer: {self.printer}\n'
              f'Scaner: {self.scaner}\n'
              f'Xerox: {self.xerox}')


rig = Equipment()

rig.info()