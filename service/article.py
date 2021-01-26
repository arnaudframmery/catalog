from sqlalchemy import desc, and_
from sqlalchemy.sql.functions import coalesce

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
        result = result.join(stmt, Article.id == stmt.c.article_id)

    if sorting_component:
        stmt = session\
            .query(Component.id,
                   coalesce(Data.value, Component.default).label('data_value'),
                   Article.id.label('article_id'))\
            .join(Catalog, Catalog.id == Component.catalog_id)\
            .join(Article, Article.catalog_id == Catalog.id)\
            .join(Data, and_(Data.component_id == Component.id, Data.article_id == Article.id), isouter=True)\
            .filter(Component.id == sorting_component)\
            .subquery()
        if sorting_direction == 'ASC':
            result = result\
                .join(stmt, stmt.c.article_id == Article.id)\
                .order_by(stmt.c.data_value)
        else:
            result = result\
                .join(stmt, stmt.c.article_id == Article.id)\
                .order_by(desc(stmt.c.data_value))

    return object_as_dict(result.all())


def get_article_detail_service(session, article_id, catalog_id):
    """recover all the data about a specific article"""
    result = session\
        .query(Component.label, coalesce(Data.value, Component.default).label('value'))\
        .join(Data, and_(Data.component_id == Component.id, Data.article_id == article_id), isouter=True)\
        .filter(Component.catalog_id == catalog_id)\
        .order_by(Component.id)\
        .all()
    return object_as_dict(result)


def delete_article_service(session, article_id):
    """delete a specific article"""
    article = session\
        .query(Article)\
        .filter(Article.id == article_id)\
        .one()
    session.delete(article)
    session.commit()
