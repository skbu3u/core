from pytest_sqlalchemy import connection, transaction, sqlalchemy_connect_url, engine

from tests.conftest import temp_database, database_exists, drop_temp_database, test_database


@temp_database
def test_exist_database():
    assert database_exists(test_database)


@temp_database
def test_url():
    assert sqlalchemy_connect_url


@temp_database
def test_engine():
    assert engine


@temp_database
def test_connection():
    assert connection


@temp_database
def test_transaction():
    assert transaction


def test_drop_database():
    drop_temp_database()
