import re
from typing import List

from pydantic import BaseModel, validator

from src.api.schemas.consumables import Consumable


class PartCreate(BaseModel):
    name: str
    price: int
    compatibility: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()

    # TODO Add price validations for parts

    @validator('compatibility')
    def compatibility_match(cls, compatibility):
        return compatibility.lower()


class Part(PartCreate):
    id: int
    contains: List[Consumable] = []

    class Config:
        orm_mode = True
