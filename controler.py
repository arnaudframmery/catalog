from service.articles import get_articles_service
from service.catalog import get_catalogs_service


class Controler:

    def __init__(self, session):
        self.session = session

    def get_catalogs(self):
        return get_catalogs_service(self.session)

    def get_articles(self, catalog_id):
        return get_articles_service(self.session, catalog_id)
