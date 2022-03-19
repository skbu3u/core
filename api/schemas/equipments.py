from pydantic import BaseModel
from api.schemas.parts import Part


class EquipmentCreate(BaseModel):
    name: str


class Equipment(EquipmentCreate):
    id: int
    parts: list[Part] = []

    class Config:
        orm_mode = True
