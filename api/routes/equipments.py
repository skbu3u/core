from fastapi import Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session
from api.schemas.equipments import Equipment, EquipmentCreate
from database.models.equipments import EquipmentModel
from database.sql import get_db


route = SQLAlchemyCRUDRouter(
    schema=Equipment,
    create_schema=EquipmentCreate,
    db_model=EquipmentModel,
    db=get_db,
    prefix='equipments',
    create_route=False,
    delete_all_route=False
)


@route.post('/')
async def create_equipment(part: EquipmentCreate, db: Session = Depends(get_db)):
    if db.query(EquipmentModel).filter(EquipmentModel.name == part.name).first():
        raise HTTPException(status_code=400, detail=f'Equipment {part.name} already exist')
    db.add(EquipmentModel(name=part.name))
    return {'msg': f'Equipment {part.name} added'}