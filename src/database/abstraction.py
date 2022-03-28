from src.database import models
from src.database.sql import Base
from src.exceptions.ClassInitializationError import ClassInitializationError

if Base and models:
    pass
else:
    raise ClassInitializationError('Need add Base, UserModel, EquipmentModel or PartModel')
