import re
from typing import List

from pydantic import BaseModel, validator

from src.api.schemas.parts import Part


class EquipmentCreate(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()


class Equipment(EquipmentCreate):
    id: int
    contains: List[Part] = []

    class Config:
        orm_mode = True
