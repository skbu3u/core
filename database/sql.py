import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if 'alembic' in sys.path[1]:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///database/sqlite.db"
else:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{sys.path[1]}/database/sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # , echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
connect = engine.connect()

