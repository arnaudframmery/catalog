from sqlalchemy import distinct, and_
from sqlalchemy.sql.functions import coalesce

from DB.tables import Type, Component, Catalog, Data, Article
from constant import FILTER_MAPPING
from service.helper import object_as_dict, object_as_list


def get_categories_service(session, component_id):
    """recover all the possible values about a specific component"""
    stmt = session\
        .query(Component.label, coalesce(Data.value, Component.default).label('value'))\
        .join(Data, Data.component_id == Component.id, isouter=True)\
        .filter(Component.id == component_id).subquery()
    result = session.query(distinct(stmt.c.value)).all()
    return object_as_list(result)


def apply_categories_service(session, catalog_id, component_id, categories):
    """recover articles about a specific catalog and a category filtering"""
    result = session\
        .query(Component.id.label('component_id'), Article.id.label('article_id'))\
        .join(Catalog, Catalog.id == Component.catalog_id)\
        .join(Article, Article.catalog_id == Catalog.id)\
        .join(Data, and_(Article.id == Data.article_id, Component.id == Data.component_id), isouter=True)\
        .filter(Component.id == component_id)\
        .filter(Catalog.id == catalog_id)\
        .filter(coalesce(Data.value, Component.default).in_(categories)).subquery()
    return result


def get_filters_service(session, catalog_id, controler):
    """recover all filters about a specific catalog"""
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


def get_all_filters_service(session):
    """recover all possible filters"""
    result = session\
        .query(Type.id, Type.code)\
        .all()
    return object_as_dict(result)
