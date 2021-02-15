from sqlalchemy import distinct, and_
from sqlalchemy.sql.functions import coalesce

from DB.tables import Filter, Component, Catalog, Value, Article
from mapping import FILTER_MAPPING
from service.helper import object_as_dict, object_as_list


def get_categories_service(session, component_id):
    """recover all the possible values about a specific component"""
    stmt = session\
        .query(Component.id, coalesce(Value.value, Component.default).label('value'))\
        .join(Catalog, Catalog.id == Component.catalog_id)\
        .join(Article, Article.catalog_id == Catalog.id)\
        .join(Value, and_(Value.component_id == Component.id, Value.article_id == Article.id), isouter=True)\
        .filter(Component.id == component_id)\
        .subquery()
    result = session.query(distinct(stmt.c.value)).all()
    return object_as_list(result)


def apply_categories_service(session, catalog_id, component_id, categories, subquery):
    """recover articles about a specific catalog and a category filtering"""
    result = session\
        .query(Component.id.label('component_id'), Article.id.label('article_id'))\
        .join(Catalog, Catalog.id == Component.catalog_id)\
        .join(Article, Article.catalog_id == Catalog.id)\
        .join(Value, and_(Article.id == Value.article_id, Component.id == Value.component_id), isouter=True)\
        .filter(Component.id == component_id)\
        .filter(Catalog.id == catalog_id)\
        .filter(coalesce(Value.value, Component.default).in_(categories)).subquery()
    if subquery:
        return result
    else:
        return object_as_dict(session.query(result.c.component_id, result.c.article_id).all())


def get_filters_service(session, catalog_id, controller):
    """recover all filters about a specific catalog"""
    components = session\
        .query(Component.id, Component.label, Filter.code)\
        .filter(Filter.id == Component.filter_id)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .order_by(Component.id)\
        .all()
    components = object_as_dict(components)

    result = []
    for a_component in components:
        if a_component['code'] in FILTER_MAPPING.keys():
            a_filter = FILTER_MAPPING[a_component['code']](controller, a_component['id'], a_component['label'])
            result.append(a_filter)

    return result


def get_all_filters_service(session):
    """recover all possible filters"""
    result = session\
        .query(Filter.id, Filter.code)\
        .all()
    return object_as_dict(result)
