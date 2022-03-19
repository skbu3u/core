from database.sql import Base
from database.models.equipment import Equipment
from database.models.users import UserModel
from exceptions.ClassInitializationError import ClassInitializationError


if Base and UserModel and Equipment:
    pass
else:
    raise ClassInitializationError('Need add Base, Users or Equipment')
