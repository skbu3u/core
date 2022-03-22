from sqlalchemy.orm import Session

from src.api.schemas.consumables import ConsumableCreate
from src.database.models.consumables import ConsumableModel


def get_consumables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConsumableModel).offset(skip).limit(limit).all()


def create_part_consumable(db: Session, consumable: ConsumableCreate, compatibility: str):
    db_consumable = ConsumableModel(**consumable.dict(), compatibility=compatibility)
    db.add(db_consumable)
    db.commit()
    db.refresh(db_consumable)
    return db_consumable
