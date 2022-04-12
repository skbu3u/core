import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database

from main import app
from src.database.sql import Base, get_db

test_database = "sqlite:///test.db"


@pytest.fixture(scope="function")
def local_session():
    # settings of test database
    engine = create_engine(test_database, connect_args={"check_same_thread": False})

    # Create test database and tables
    if not database_exists(test_database):
        Base.metadata.create_all(engine)

    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield local_session


def temp_database(f):
    def func(local_session, *args, **kwargs):
        # Session maker instance to connect to test DB
        #  (local_session)From fixture

        def override_get_db():
            try:
                session = local_session()
                yield session
                session.commit()
            finally:
                session.close()

        # get to use local_session received from fixture_Force db change
        app.dependency_overrides[get_db] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # get_Undo db
        app.dependency_overrides[get_db] = get_db
    return func


def drop_temp_database():
    # Test database already exists
    assert database_exists(test_database)
    # Drop the test database
    drop_database(test_database)


def user_authorization(test_client):
    test_client.post("/security/register", json={
        "id": 1,
        "name": "test_user",
        "password": "test_password"})
    response = test_client.post("/security/login", json={
        "name": "test_user",
        "password": "test_password"}
    )
    assert response.status_code == 200
    data = response.json()
    token = data[1]["token"]
    assert data[0]["name"] == "test_user"
    return {"Authorization": f"Bearer {token}"}
