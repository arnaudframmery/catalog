import os

from DB.tables import Catalog, Article, Component, Filter, Value, ValueType
from constant import VALUE_TYPE_CODE, FILTER_CODE


def populate_init(session):
    filter_base = Filter(code=FILTER_CODE.NO_FILTER)
    filter_cat = Filter(code=FILTER_CODE.CATEGORY)

    value_type_text = ValueType(code=VALUE_TYPE_CODE.TEXT)
    value_type_int = ValueType(code=VALUE_TYPE_CODE.INT)
    value_type_float = ValueType(code=VALUE_TYPE_CODE.FLOAT)
    value_type_image = ValueType(code=VALUE_TYPE_CODE.IMAGE)

    session.add(filter_base)
    session.add(filter_cat)

    session.add(value_type_text)
    session.add(value_type_int)
    session.add(value_type_float)
    session.add(value_type_image)

    session.commit()


def populate_light(session):
    """inject some value into the database"""
    resource_path = os.path.join(os.getcwd(), 'resource')

    people = Catalog(name='people', theme='base')
    cities = Catalog(name='cities', theme='base')

    article_1 = Article(title='Harry Potter')
    article_2 = Article(title='Ron Weasley')
    article_3 = Article(title='Hermione Granger')
    article_4 = Article(title='Drago Malefoy')

    article_cities = Article(title='Paris')

    component_1 = Component(label='Last name', default='Smith', is_sortable=True)
    component_2 = Component(label='First name', default='John', is_sortable=True)
    component_3 = Component(label='Gender', default='Male')
    component_4 = Component(label='Age', default='18', is_sortable=True)
    component_5 = Component(label='House', default='Gryffindor')
    component_6 = Component(label='Grade', default='10.0', is_sortable=True)
    component_7 = Component(label='Photo', default=os.path.join(resource_path, 'hagrid.jpg'))
    components = [component_1, component_2, component_3, component_4, component_5, component_6, component_7]

    filter_base = session.query(Filter).filter(Filter.code == FILTER_CODE.NO_FILTER).one()
    filter_cat = session.query(Filter).filter(Filter.code == FILTER_CODE.CATEGORY).one()

    value_type_text = session.query(ValueType).filter(ValueType.code == VALUE_TYPE_CODE.TEXT).one()
    value_type_int = session.query(ValueType).filter(ValueType.code == VALUE_TYPE_CODE.INT).one()
    value_type_float = session.query(ValueType).filter(ValueType.code == VALUE_TYPE_CODE.FLOAT).one()
    value_type_image = session.query(ValueType).filter(ValueType.code == VALUE_TYPE_CODE.IMAGE).one()

    value_1_lname = Value(value='Potter')
    value_1_fname = Value(value='Harry')
    value_1_gender = Value(value='Male')
    value_1_age = Value(value='17')
    value_1_house = Value(value='Gryffindor')
    value_1_grade = Value(value='13.8')
    value_1_photo = Value(value=os.path.join(resource_path, 'harry_potter.jpg'))

    value_2_lname = Value(value='Weasley')
    value_2_fname = Value(value='Ron')
    value_2_gender = Value(value='Male')
    value_2_age = Value(value='18')
    value_2_house = Value(value='Gryffindor')
    value_2_grade = Value(value='11.0')
    value_2_photo = Value(value=os.path.join(resource_path, 'ron_weasley.jpg'))

    value_3_lname = Value(value='Granger')
    value_3_fname = Value(value='Hermione')
    value_3_gender = Value(value='Female')
    value_3_age = Value(value='16')
    value_3_house = Value(value='Gryffindor')
    value_3_grade = Value(value='18.4')
    value_3_photo = Value(value=os.path.join(resource_path, 'hermione_granger.jpg'))

    value_4_lname = Value(value='Malefoy')
    value_4_fname = Value(value='Drago')
    value_4_gender = Value(value='Male')
    value_4_age = Value(value='17')
    value_4_house = Value(value='Slytherin')
    value_4_grade = Value(value='12.9')
    value_4_photo = Value(value=os.path.join(resource_path, 'drago_malefoy.jpg'))

    value_1 = [value_1_lname, value_1_fname, value_1_gender, value_1_age, value_1_house, value_1_grade, value_1_photo]
    value_2 = [value_2_lname, value_2_fname, value_2_gender, value_2_age, value_2_house, value_2_grade, value_2_photo]
    value_3 = [value_3_lname, value_3_fname, value_3_gender, value_3_age, value_3_house, value_3_grade, value_3_photo]
    value_4 = [value_4_lname, value_4_fname, value_4_gender, value_4_age, value_4_house, value_4_grade, value_4_photo]

    people.article = [article_1, article_2, article_3, article_4]
    cities.article = [article_cities]

    for a_component in [component_1, component_2, component_4, component_6, component_7]:
        a_component.filter_id = filter_base.id
    for a_component in [component_3, component_5]:
        a_component.filter_id = filter_cat.id

    for a_component in [component_1, component_2, component_3, component_5]:
        a_component.value_type_id = value_type_text.id
    for a_component in [component_4]:
        a_component.value_type_id = value_type_int.id
    for a_component in [component_6]:
        a_component.value_type_id = value_type_float.id
    for a_component in [component_7]:
        a_component.value_type_id = value_type_image.id

    people.component = components

    for a_component, a_value in zip(components, value_1):
        a_component.value.append(a_value)
    for a_component, a_value in zip(components, value_2):
        a_component.value.append(a_value)
    for a_component, a_value in zip(components, value_3):
        a_component.value.append(a_value)
    for a_component, a_value in zip(components, value_4):
        a_component.value.append(a_value)

    article_1.value = value_1
    article_2.value = value_2
    article_3.value = value_3
    article_4.value = value_4

    session.add(people)
    session.add(cities)
    session.commit()
