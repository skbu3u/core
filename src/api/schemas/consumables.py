import re

from pydantic import BaseModel, validator


class ConsumableBase(BaseModel):
    name: str
    price: int


class ConsumableCreate(ConsumableBase):
    @validator('name')
    def name_match(cls, name):
        if re.match(r'^[а-яА-Я.,!@#$%^&/+=]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower().title()


class Consumable(ConsumableBase):
    id: int
    compatibility: str

    class Config:
        orm_mode = True
