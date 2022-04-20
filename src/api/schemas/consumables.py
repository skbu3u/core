import re

from pydantic import BaseModel, validator


class ConsumableCreate(BaseModel):
    name: str
    price: int
    compatibility: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()

    # TODO Add price validations for consumables

    @validator('compatibility')
    def compatibility_match(cls, compatibility):
        return compatibility.lower()


class Consumable(ConsumableCreate):
    id: int

    class Config:
        orm_mode = True
