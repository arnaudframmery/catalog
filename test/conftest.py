# this code comes from kissgyorgy/sqlalchemy_conftest.py on github
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import DB.tables
import pytest

from DB.populate import populate_init
from controller import Controller


component_input_1 = {
    'label': 'component_1',
    'default_value': 'default_value_1',
    'is_sortable': False,
    'filter_code': 'no filter',
}
component_input_2 = {
    'label': 'component_2',
    'default_value': 'default_value_2',
    'is_sortable': True,
    'filter_code': 'category',
}


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
def controller(dbsession):
    """Only the init db"""
    populate_init(dbsession)
    return Controller(dbsession)


@pytest.fixture
def ctrl_base_1(controller):
    """Only 2 catalogs in db"""
    controller.create_catalog('test_1')
    controller.create_catalog('test_2')
    return controller


@pytest.fixture
def ctrl_base_2(ctrl_base_1):
    """Only ctrl_base_1 elements + 2 articles and 3 components in db"""
    ctrl_base_1.create_article(1, 'title_1')
    ctrl_base_1.create_article(2, 'title_2')
    ctrl_base_1.create_components(1, [component_input_1])
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    return ctrl_base_1


@pytest.fixture
def ctrl_base_3(ctrl_base_2):
    """Only ctrl_base_1 elements + ctrl_base_1 elements + 2 articles and 3 values in db"""
    ctrl_base_2.create_article(2, 'title_3')
    ctrl_base_2.create_article(2, 'title_4')
    ctrl_base_2.create_values([
        {'component_id': 1, 'value': 'value_1', 'article_id': 1},
        {'component_id': 2, 'value': 'value_2', 'article_id': 2},
        {'component_id': 3, 'value': 'value_3', 'article_id': 2},
    ])
    return ctrl_base_2
