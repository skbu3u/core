import re

from pydantic import BaseModel, validator


class ConsumableBase(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower()

    price: int


class ConsumableCreate(ConsumableBase):
    compatibility: str

    @validator('compatibility')
    def compatibility_match(cls, compatibility):
        return compatibility.lower()


class Consumable(ConsumableBase):
    id: int

    class Config:
        orm_mode = True
