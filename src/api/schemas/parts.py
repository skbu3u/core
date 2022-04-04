import re
from typing import List

from pydantic import BaseModel, validator

from src.api.schemas.consumables import Consumable


class PartBase(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()

    price: int
    # TODO Add price validations


class PartCreate(PartBase):
    compatibility: str

    @validator('compatibility')
    def compatibility_match(cls, compatibility):
        return compatibility.lower()


class Part(PartBase):
    id: int
    contains: List[Consumable] = []

    class Config:
        orm_mode = True
