from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.schemas.equipments import Equipment, EquipmentCreate
from src.database.crud.equipments import get_equipment_by_name, create_equipment, get_equipments, get_equipment
from src.database.sql import get_db

route = APIRouter()


@route.post("/equipments/", response_model=Equipment)
def create_equipments(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = get_equipment_by_name(db, name=equipment.name)
    if db_equipment:
        raise HTTPException(status_code=400, detail=f"{equipment.name} already exist")
    equipments = create_equipment(db=db, equipment=equipment)
    return equipments


@route.get("/equipments/", response_model=list[Equipment])
def get_all_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipments = get_equipments(db, skip=skip, limit=limit)
    return equipments


@route.get("/equipments/{equipment_id}", response_model=Equipment)
def get_one_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = get_equipment(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment
