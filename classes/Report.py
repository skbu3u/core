from classes.Equipment import *
from exceptions.ClassInitializationError import *


class Report:

    def __init__(self, equipment):
        if isinstance(equipment, Equipment):
            self.info = equipment.dict
        else:
            raise ClassInitializationError('Equipment must be Equipment class')
