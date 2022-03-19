from sqlalchemy import Column, String, Integer, Boolean
from database.sql import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


users = Users.__table__
