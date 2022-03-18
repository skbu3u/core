from sqlalchemy import Column, String, Integer, Boolean
from database.sql import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True, unique=True)  # autoincrement=True, nullable=True
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(Boolean)


users = Users.__table__
