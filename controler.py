from service.article import get_articles_service, get_article_detail_service
from service.catalog import get_catalogs_service
from service.filter import get_filters_service, get_categories_service, apply_categories_service


class Controler:

    def __init__(self, session):
        self.session = session

    def get_catalogs(self):
        return get_catalogs_service(self.session)

    def get_articles(self, catalog_id, filters):
        return get_articles_service(self.session, catalog_id, filters)

    def get_article_detail(self, article_id):
        return get_article_detail_service(self.session, article_id)

    def get_filters(self, catalog_id):
        return get_filters_service(self.session, catalog_id, self)

    def get_categories(self, component_id):
        return get_categories_service(self.session, component_id)

    def apply_categories(self, catalog_id, component_id, categories):
        return apply_categories_service(self.session, catalog_id, component_id, categories)
