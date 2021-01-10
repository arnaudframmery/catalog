from DB.tables import Catalog, Article
from service.helper import object_as_dict


def get_articles_service(session, catalog_id):
    return object_as_dict(session.query(Article.id, Article.title).join(Catalog).filter(Catalog.id == catalog_id).all())
