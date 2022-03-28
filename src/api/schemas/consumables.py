import re

from pydantic import BaseModel, validator


class ConsumableBase(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w\s.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower().title()

    price: int


class ConsumableCreate(ConsumableBase):
    pass


class Consumable(ConsumableBase):
    id: int
    compatibility: int

    class Config:
        orm_mode = True
