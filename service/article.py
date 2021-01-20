from sqlalchemy import desc

from DB.tables import Catalog, Article, Data, Component
from service.helper import object_as_dict


def get_articles_service(session, catalog_id, filters, sorting_component, sorting_direction):
    """recover articles about a specific catalog, with filtering and sorting options"""
    result = session\
        .query(Article.id, Article.title)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)

    for a_filter in filters:
        stmt = a_filter.apply_filter(catalog_id)
        result = result.join(stmt, Article.id == stmt.c.id)

    if sorting_component:
        if sorting_direction == 'ASC':
            result = result\
                .join(Data, Article.id == Data.article_id)\
                .filter(Data.component_id == sorting_component)\
                .order_by(Data.value)
        else:
            result = result\
                .join(Data, Article.id == Data.article_id)\
                .filter(Data.component_id == sorting_component)\
                .order_by(desc(Data.value))

    return object_as_dict(result.all())


def get_article_detail_service(session, article_id):
    """recover all the data about a specific article"""
    result = session\
        .query(Data.value, Component.label)\
        .filter(Data.component_id == Component.id)\
        .filter(Data.article_id == article_id)\
        .order_by(Component.id)\
        .all()
    return object_as_dict(result)
