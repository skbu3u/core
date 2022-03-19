from fastapi_crudrouter import SQLAlchemyCRUDRouter
from api.schemas.equipments import Equipment, EquipmentCreate
from database.models.equipments import EquipmentModel
from database.sql import get_db


route = SQLAlchemyCRUDRouter(
    schema=Equipment,
    create_schema=EquipmentCreate,
    db_model=EquipmentModel,
    db=get_db,
    prefix='equipments'
)
