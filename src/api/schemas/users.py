import re

from fastapi import Query
from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    name: str = Query(...,
                      title='Enter name',
                      description='Input can contain latin letters and numbers',
                      max_length=16,
                      min_length=3,
                      strip_whitespace=True)

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name

    email: str = Query(...,
                       title='Enter email',
                       description='Input can contain latin letters and numbers',
                       max_length=30,
                       min_length=5,
                       strip_whitespace=True)

    @validator('email')
    def email_match(cls, email):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            raise ValueError(f"Email '{email}' is incorrect")
        return email

    password: str = Query(...,
                          title='Enter password',
                          description='Input can contain latin letters, numbers and special characters',
                          min_length=5,
                          strip_whitespace=True)

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
