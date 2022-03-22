from src.classes.Equipment import Equipment
from src.exceptions.ClassInitializationError import ClassInitializationError


class Report:

    def __init__(self, equipment):
        if isinstance(equipment, Equipment):
            self.info = equipment.get_parts
        else:
            raise ClassInitializationError('Equipment must be Equipment class')
