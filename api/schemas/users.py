from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    email: str
    password: str


class User(AuthDetails):
    about: str