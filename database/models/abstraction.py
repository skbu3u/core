from database.sql import Base
from database.models.users import UserModel
from database.models.equipments import EquipmentModel
from database.models.parts import PartModel
from exceptions.ClassInitializationError import ClassInitializationError


if Base and UserModel and EquipmentModel and PartModel:
    pass
else:
    raise ClassInitializationError('Need add Base, UserModel, EquipmentModel or PartModel')
