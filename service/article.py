from sqlalchemy import and_
from sqlalchemy.sql.functions import coalesce

from DB.tables import Catalog, Article, Value, Component, ValueType
from constant import VALUE_TYPE_MAPPING
from service.helper import object_as_dict


def get_articles_service(session, catalog_id, filters, sorting_component, sorting_direction, sorting_code):
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
                   coalesce(Value.value, Component.default).label('value_value'),
                   Article.id.label('article_id'))\
            .join(Catalog, Catalog.id == Component.catalog_id)\
            .join(Article, Article.catalog_id == Catalog.id)\
            .join(Value, and_(Value.component_id == Component.id, Value.article_id == Article.id), isouter=True)\
            .filter(Component.id == sorting_component)\
            .subquery()
        result = VALUE_TYPE_MAPPING[sorting_code].sort_subquery(result, stmt, sorting_direction)

    return object_as_dict(result.all())


def get_article_detail_service(session, article_id, catalog_id):
    """recover all the values about a specific article"""
    result = session\
        .query(Component.label,
               coalesce(Value.value, Component.default).label('value'),
               Component.id.label('component_id'),
               Value.id.label('value_id'),
               ValueType.code.label('code'))\
        .join(Value, and_(Value.component_id == Component.id, Value.article_id == article_id), isouter=True)\
        .join(ValueType, ValueType.id == Component.value_type_id)\
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


def update_article_service(session, article_id, title):
    """update a specific article"""
    article = session\
        .query(Article)\
        .filter(Article.id == article_id)\
        .one()
    article.title = title
    session.commit()


def create_article_service(session, catalog_id, title):
    new_article = Article(title=title, catalog_id=catalog_id)
    session.add(new_article)
    session.commit()
    return new_article.id
