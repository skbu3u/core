import re
from fastapi import Query
from pydantic import BaseModel, validator


class User(BaseModel):
    username: str = Query(...,
                          title='Enter name',
                          description='Input can contain latin letters and numbers',
                          min_length=3,
                          max_length=16,
                          strip_whitespace=True)

    @validator('username')
    def name_match(cls, username):
        if not re.match(r'^[\w.-]+$', username):
            raise ValueError(f"Name '{username}' is incorrect")
        return username

    email: str = Query(...,
                       title='Enter email',
                       description='Input can contain latin letters and numbers',
                       min_length=5,
                       max_length=30,
                       strip_whitespace=True)

    @validator('email')
    def email_match(cls, email):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            raise ValueError(f"Email '{email}' is incorrect")
        return  email

    password: str = Query(...,
                          title='Enter password',
                          description='Input can contain latin letters, numbers and special characters',
                          min_length=5,
                          strip_whitespace=True)

    @validator('password')
    def password_match(cls, password):
        if not re.match(r'^[\w.!@#$%^&+=-]+$', password):
            raise ValueError(f"Password '{password}' is incorrect")
        return password


class Role(User):
    is_admin: bool
