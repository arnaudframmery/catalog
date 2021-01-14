from DB.tables import Catalog, Article, Data, Component
from service.helper import object_as_dict


def get_articles_service(session, catalog_id):
    result = session\
        .query(Article.id, Article.title)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .all()
    return object_as_dict(result)


def get_article_detail_service(session, article_id):
    result = session\
        .query(Data.value, Component.label)\
        .filter(Data.component_id == Component.id)\
        .filter(Data.article_id == article_id)\
        .order_by(Component.id)\
        .all()
    return object_as_dict(result)
