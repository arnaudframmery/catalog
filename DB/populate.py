from DB.tables import Catalog, Article, Component, Type, Data


def populate_light(session):
    people = Catalog(name='people', theme='base')
    cities = Catalog(name='cities', theme='base')

    article_1 = Article(title='001')
    article_2 = Article(title='002')
    article_3 = Article(title='003')
    article_cities = Article(title='Paris')

    component_1 = Component(label='Last name', default='Smith', is_sortable=True)
    component_2 = Component(label='First name', default='John', is_sortable=True)
    component_3 = Component(label='Gender', default='Male')
    components = [component_1, component_2, component_3]

    type_1 = Type(code='simple')
    type_cat = Type(code='category')

    data_1_lname = Data(value='Potter')
    data_1_fname = Data(value='Harry')
    data_1_gender = Data(value='Male')
    data_2_lname = Data(value='Weasley')
    data_2_fname = Data(value='Ron')
    data_2_gender = Data(value='Male')
    data_3_lname = Data(value='Granger')
    data_3_fname = Data(value='Hermione')
    data_3_gender = Data(value='Female')
    data_1 = [data_1_lname, data_1_fname, data_1_gender]
    data_2 = [data_2_lname, data_2_fname, data_2_gender]
    data_3 = [data_3_lname, data_3_fname, data_3_gender]

    people.article = [article_1, article_2, article_3]
    cities.article = [article_cities]
    type_1.component = [component_1, component_2]
    type_cat.component = [component_3]
    people.component = [component_1, component_2, component_3]

    for a_component, a_data in zip(components, data_1):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_2):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_3):
        a_component.data.append(a_data)

    article_1.data = data_1
    article_2.data = data_2
    article_3.data = data_3

    session.add(people)
    session.add(cities)
    session.commit()
