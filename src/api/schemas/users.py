import re

from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    name: str
    password: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name

    @validator('password')
    def password_match(cls, password):
        if not re.match(r'^[\w.!@#$%^&/+=-]+$', password):
            raise ValueError(f"Password '{password}' is incorrect")
        return password


class User(UserCreate):
    id: int
    is_admin: bool = False

    class Config:
        orm_mode = True
