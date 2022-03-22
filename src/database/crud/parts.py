from sqlalchemy.orm import Session

from src.api.schemas.parts import PartCreate
from src.database.models.parts import PartModel


def get_parts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PartModel).offset(skip).limit(limit).all()


def create_equipment_part(db: Session, part: PartCreate, compatibility: str):
    db_part = PartModel(**part.dict(), compatibility=compatibility)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part
