from sqlalchemy.orm import Session

from src.api.schemas.equipments import EquipmentCreate
from src.database.models.equipments import EquipmentModel


def get_equipment(db: Session, equipment_id: int):
    return db.query(EquipmentModel).filter(EquipmentModel.id == equipment_id).first()


def get_equipment_by_name(db: Session, name: str):
    return db.query(EquipmentModel).filter(EquipmentModel.name == name).first()


def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EquipmentModel).offset(skip).limit(limit).all()


def create_equipment(db: Session, equipment: EquipmentCreate):
    db_equipment = EquipmentModel(name=equipment.name)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment
