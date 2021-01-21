from DB.tables import Catalog, Article, Component, Type, Data


def populate_light(session):
    """inject some data into the database"""

    people = Catalog(name='people', theme='base')
    cities = Catalog(name='cities', theme='base')

    article_1 = Article(title='Harry Potter')
    article_2 = Article(title='Ron Weasley')
    article_3 = Article(title='Hermione Granger')
    article_4 = Article(title='Drago Malfoy')
    article_cities = Article(title='Paris')

    component_1 = Component(label='Last name', default='Smith', is_sortable=True)
    component_2 = Component(label='First name', default='John', is_sortable=True)
    component_3 = Component(label='Gender', default='Male')
    component_4 = Component(label='Age', default='18', is_sortable=True)
    component_5 = Component(label='House', default='Gryffindor')
    components = [component_1, component_2, component_3, component_4, component_5]

    type_1 = Type(code='simple')
    type_cat = Type(code='category')

    data_1_lname = Data(value='Potter')
    data_1_fname = Data(value='Harry')
    data_1_gender = Data(value='Male')
    data_1_age = Data(value='17')
    data_1_house = Data(value='Gryffindor')

    data_2_lname = Data(value='Weasley')
    data_2_fname = Data(value='Ron')
    data_2_gender = Data(value='Male')
    data_2_age = Data(value='18')
    data_2_house = Data(value='Gryffindor')

    data_3_lname = Data(value='Granger')
    data_3_fname = Data(value='Hermione')
    data_3_gender = Data(value='Female')
    data_3_age = Data(value='16')
    data_3_house = Data(value='Gryffindor')

    data_4_lname = Data(value='Malefoy')
    data_4_fname = Data(value='Drago')
    data_4_gender = Data(value='Male')
    data_4_age = Data(value='17')
    data_4_house = Data(value='Slytherin')

    data_1 = [data_1_lname, data_1_fname, data_1_gender, data_1_age, data_1_house]
    data_2 = [data_2_lname, data_2_fname, data_2_gender, data_2_age, data_2_house]
    data_3 = [data_3_lname, data_3_fname, data_3_gender, data_3_age, data_3_house]
    data_4 = [data_4_lname, data_4_fname, data_4_gender, data_4_age, data_4_house]

    people.article = [article_1, article_2, article_3, article_4]
    cities.article = [article_cities]
    type_1.component = [component_1, component_2, component_4]
    type_cat.component = [component_3, component_5]
    people.component = components

    for a_component, a_data in zip(components, data_1):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_2):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_3):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_4):
        a_component.data.append(a_data)

    article_1.data = data_1
    article_2.data = data_2
    article_3.data = data_3
    article_4.data = data_4

    session.add(people)
    session.add(cities)
    session.commit()
