from pytest_sqlalchemy import connection

from tests.conftest import temp_database, database_exists, drop_temp_database


@temp_database
def test_connection():
    assert connection


def test_exist_database():
    assert database_exists("sqlite:///test.db")


def test_drop_database():
    drop_temp_database()
    