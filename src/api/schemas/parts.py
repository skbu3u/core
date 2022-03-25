import re
from typing import Optional

from pydantic import BaseModel, validator

from src.api.schemas.consumables import Consumable


class PartBase(BaseModel):
    name: str
    price: int


class PartCreate(PartBase):
    @validator('name')
    def name_match(cls, name):
        if re.match(r'^[а-яА-Я.,!@#$%^&/+=]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower().title()


class Part(PartBase):
    id: int
    compatibility: str
    consumables: Optional[list[Consumable]] = []

    class Config:
        orm_mode = True
