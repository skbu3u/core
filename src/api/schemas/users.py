import re

from fastapi import Query
from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name

    email: str

    @validator('email')
    def email_match(cls, email):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            raise ValueError(f"Email '{email}' is incorrect")
        return email

    password: str

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


class UserLogin(BaseModel):
    email: str
    password: str
