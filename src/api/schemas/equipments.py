import re
from typing import List

from pydantic import BaseModel, validator

from src.api.schemas.parts import Part


class EquipmentBase(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()


class EquipmentCreate(EquipmentBase):
    pass


class Equipment(EquipmentBase):
    id: int
    contains: List[Part] = []

    class Config:
        orm_mode = True
