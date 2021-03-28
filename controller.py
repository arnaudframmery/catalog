from service.article import get_articles_service, get_article_detail_service, delete_article_service, \
    update_article_service, create_article_service
from service.catalog import get_catalogs_service, create_catalog_service, delete_catalog_service
from service.component import get_components_service, create_components_service, update_components_service, \
    delete_components_service, get_sortable_components_service, update_component_display_setting_service
from service.value import create_values_service, update_values_service, get_values_service, delete_value_service
from service.filter import get_filters_service, get_categories_service, apply_categories_service, \
    get_all_filters_service
from service.value_type import get_all_value_types_service


class Controller:
    """
    give access to the different services
    """

    def __init__(self, session):
        self.session = session

    # Catalogs
    def create_catalog(self, catalog_name):
        return create_catalog_service(self.session, catalog_name)

    def get_catalogs(self):
        return get_catalogs_service(self.session)

    def delete_catalog(self, catalog_id):
        delete_catalog_service(self.session, catalog_id)

    # Components
    def create_components(self, catalog_id, components_data):
        create_components_service(self.session, catalog_id, components_data)

    def update_components(self, components_data):
        return update_components_service(self.session, components_data)

    def update_component_display_setting(self, id, from_row, from_column, row_span, column_span):
        return update_component_display_setting_service(self.session, id, from_row, from_column, row_span, column_span)

    def get_components(self, catalog_id):
        return get_components_service(self.session, catalog_id)

    def get_sortable_components(self, catalog_id):
        return get_sortable_components_service(self.session, catalog_id)

    def delete_components(self, components_id):
        delete_components_service(self.session, components_id)

    # Articles
    def create_article(self, catalog_id, title):
        return create_article_service(self.session, catalog_id, title)

    def update_article(self, article_id, title):
        update_article_service(self.session, article_id, title)

    def get_articles(self, catalog_id, filters, sorting_component, sorting_direction, sorting_code):
        return get_articles_service(
            self.session,
            catalog_id,
            filters,
            sorting_component,
            sorting_direction,
            sorting_code,
        )

    def get_article_detail(self, article_id, catalog_id):
        return get_article_detail_service(self.session, article_id, catalog_id)

    def delete_article(self, article_id):
        delete_article_service(self.session, article_id)

    # Values
    def create_values(self, value_list):
        create_values_service(self.session, value_list)

    def update_values(self, value_list):
        update_values_service(self.session, value_list)

    def get_values(self, component_id):
        return get_values_service(self.session, component_id)

    def delete_value_service(self, value_id):
        delete_value_service(self.session, value_id)

    # Filters
    def get_all_filters(self):
        return get_all_filters_service(self.session)

    def get_filters(self, catalog_id):
        return get_filters_service(self.session, catalog_id, self)

    def get_categories(self, component_id):
        return get_categories_service(self.session, component_id)

    def apply_categories(self, catalog_id, component_id, categories, subquery=True):
        return apply_categories_service(self.session, catalog_id, component_id, categories, subquery)

    # Value types
    def get_all_value_types(self):
        return get_all_value_types_service(self.session)
