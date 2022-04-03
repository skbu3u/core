from src.database import models
from src.database.sql import Base

if Base and models:
    pass
else:
    raise NameError('Need add Base, UserModel, EquipmentModel or PartModel')
