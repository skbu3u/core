import sys
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

is_database = sorted(Path(sys.path[1]).glob('**/sqlite.db'))
if is_database:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{sys.path[1]}/src/database/sqlite.db"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///src/database/sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
