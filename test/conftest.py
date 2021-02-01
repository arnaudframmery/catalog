# this code comes from kissgyorgy/sqlalchemy_conftest.py on github
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import DB.tables
import pytest

from controler import Controler


@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite://")


@pytest.fixture(scope="session")
def tables(engine):
    DB.tables.Base.metadata.create_all(engine)
    yield
    DB.tables.Base.metadata.drop_all(engine)


@pytest.fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture
def controler(dbsession):
    """Returns a controler"""
    return Controler(dbsession)
