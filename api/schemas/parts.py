from pydantic import BaseModel


class PartCreate(BaseModel):
    name: str
    price: int
    compatibility: str


class Part(PartCreate):
    id: int
    parts: list[str] = []

    class Config:
        orm_mode = True
