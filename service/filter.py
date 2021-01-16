from sqlalchemy import distinct

from DB.tables import Type, Component, Catalog, Data, Article
from constant import FILTER_MAPPING
from service.helper import object_as_dict, object_as_list


def get_categories_service(session, component_id):
    result = session\
        .query(distinct(Data.value))\
        .join(Component)\
        .filter(Component.id == component_id)\
        .all()
    return object_as_list(result)


def apply_categories_service(session, catalog_id, component_id, categories):
    result = session\
        .query(Article.id)\
        .join(Catalog, Article.catalog_id == Catalog.id)\
        .join(Data, Article.id == Data.article_id)\
        .join(Component, Data.component_id == Component.id)\
        .filter(Catalog.id == catalog_id)\
        .filter(Component.id == component_id)\
        .filter(Data.value.in_(categories))\
        .subquery()
    return result


def get_filters_service(session, catalog_id, controler):
    components = session\
        .query(Component.id, Component.label, Type.code)\
        .filter(Type.id == Component.type_id)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .order_by(Component.id)\
        .all()
    components = object_as_dict(components)

    result = []
    for a_component in components:
        if a_component['code'] in FILTER_MAPPING.keys():
            a_filter = FILTER_MAPPING[a_component['code']](controler, a_component['id'], a_component['label'])
            result.append(a_filter)

    return result
