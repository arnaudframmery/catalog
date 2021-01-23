from service.article import get_articles_service, get_article_detail_service
from service.catalog import get_catalogs_service, create_catalog_service
from service.component import get_components_service, create_components_service, update_components_service, \
    delete_components_service
from service.filter import get_filters_service, get_categories_service, apply_categories_service, \
    get_all_filters_service
from service.sorting import get_sortable_components_service


class Controler:
    """
    give access to the different services
    """

    def __init__(self, session):
        self.session = session

    def get_catalogs(self):
        return get_catalogs_service(self.session)

    def get_articles(self, catalog_id, filters, sorting_component, sorting_direction):
        return get_articles_service(self.session, catalog_id, filters, sorting_component, sorting_direction)

    def get_article_detail(self, article_id, catalog_id):
        return get_article_detail_service(self.session, article_id, catalog_id)

    def get_filters(self, catalog_id):
        return get_filters_service(self.session, catalog_id, self)

    def get_categories(self, component_id):
        return get_categories_service(self.session, component_id)

    def apply_categories(self, catalog_id, component_id, categories):
        return apply_categories_service(self.session, catalog_id, component_id, categories)

    def get_sortable_components(self, catalog_id):
        return get_sortable_components_service(self.session, catalog_id)

    def get_components(self, catalog_id):
        return get_components_service(self.session, catalog_id)

    def get_all_filters(self):
        return get_all_filters_service(self.session)

    def create_catalog(self, catalog_name):
        return create_catalog_service(self.session, catalog_name)

    def create_components(self, catalog_id, components_data):
        return create_components_service(self.session, catalog_id, components_data)

    def update_components(self, components_data):
        return update_components_service(self.session, components_data)

    def delete_components(self, components_id):
        return delete_components_service(self.session, components_id)
