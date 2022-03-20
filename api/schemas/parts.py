from pydantic import BaseModel
from typing import Optional, List, Union, Dict


class PartCreate(BaseModel):
    name: str
    price: int
    compatibility: Optional[List[str]] = []


class Part(PartCreate):
    id: int

    class Config:
        orm_mode = True


class PartUpdate(Part):
    parts: Union[Part, Dict] = []

    class Config:
        orm_mode = True
