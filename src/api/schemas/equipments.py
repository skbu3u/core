from pydantic import BaseModel
from src.api.schemas.parts import Part
from typing import Optional, List


class EquipmentCreate(BaseModel):
    name: str


class Equipment(EquipmentCreate):
    id: int
    parts: Optional[List[Part]] = []

    class Config:
        orm_mode = True
