from src.database.models.consumables import ConsumableModel
from src.database.models.equipments import EquipmentModel
from src.database.models.parts import PartModel
from src.database.models.users import UserModel
from src.database.sql import Base
from src.exceptions.ClassInitializationError import ClassInitializationError

if Base and UserModel and EquipmentModel and PartModel and ConsumableModel:
    pass
else:
    raise ClassInitializationError('Need add Base, UserModel, EquipmentModel or PartModel')
