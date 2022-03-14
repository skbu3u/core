from database.sql import Base
from database.models.equipment import Equipment
from exceptions.ClassInitializationError import ClassInitializationError


if Base and Equipment:
    pass
else:
    raise ClassInitializationError('Need add Base or Equipment')
