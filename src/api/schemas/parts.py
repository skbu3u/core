import re
from typing import List

from pydantic import BaseModel, validator

from src.api.schemas.consumables import Consumable


class PartBase(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower().title()

    price: int
    # TODO Add price validations


class PartCreate(PartBase):
    pass


class Part(PartBase):
    id: int
    compatibility: str
    consumables: List[Consumable] = []

    class Config:
        orm_mode = True
