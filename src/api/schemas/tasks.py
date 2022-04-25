import re
from typing import List, Optional

from pydantic import BaseModel, validator


class TaskCreate(BaseModel):
    name: str

    @validator('name')
    def name_match(cls, name):
        if not re.match(r'^[\w.-]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name


class Task(TaskCreate):
    id: int
    contains: Optional[List] = []

    class Config:
        orm_mode = True
