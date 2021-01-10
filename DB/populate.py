from DB.tables import Catalog, Article, Component, Type, Data


def populate_light(session):
    people = Catalog(name='people', theme='base')
    cities = Catalog(name='cities', theme='base')

    article_1 = Article(title='001')
    article_2 = Article(title='002')
    article_cities = Article(title='Paris')

    component_1 = Component(label='Nom', default='Smith')
    component_2 = Component(label='Prénom', default='John')
    component_3 = Component(label='Gender', default='Male')
    components = [component_1, component_2, component_3]

    type_1 = Type(code='simple')

    data_1_nom = Data(value='Potter')
    data_1_prenom = Data(value='Harry')
    data_1_gender = Data(value='Male')
    data_2_nom = Data(value='Weasley')
    data_2_prenom = Data(value='Ron')
    data_2_gender = Data(value='Male')
    data_1 = [data_1_nom, data_1_prenom, data_1_gender]
    data_2 = [data_2_nom, data_2_prenom, data_2_gender]

    people.article = [article_1, article_2]
    cities.article = [article_cities]
    type_1.component = [component_1, component_2, component_3]
    people.component = [component_1, component_2, component_3]

    for a_component, a_data in zip(components, data_1):
        a_component.data.append(a_data)
    for a_component, a_data in zip(components, data_2):
        a_component.data.append(a_data)

    article_1.data = data_1
    article_2.data = data_2

    session.add(people)
    session.add(cities)
    session.commit()
