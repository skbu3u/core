class Equipment:
    name = 'Equipment'
    printer = False
    scaner = False
    xerox = False

    def info(self):
        if self.printer:
            self.name = 'part for printer'
        elif self.scaner:
            self.name = 'part for scaner'
        elif self.xerox:
            self.name = 'part for xerox'
        name = f'Spare {self.name}'
        print(name)
        return name


class Printer(Equipment):
    printer = True


class Scaner(Equipment):
    scaner = True


class Xerox(Equipment):
    xerox = True


class PrinterPart(Printer):

    def some_method(self):
        pass


class ScanerPart(Scaner):

    def some_method(self):
        pass


class XeroxPart(Xerox):

    def some_method(self):
        pass
