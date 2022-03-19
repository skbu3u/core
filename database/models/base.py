from database.sql import Base
from database.models.equipment import Equipment
from database.models.users import Users
from exceptions.ClassInitializationError import ClassInitializationError


if Base and Users and Equipment:
    pass
else:
    raise ClassInitializationError('Need add Base, Users or Equipment')
