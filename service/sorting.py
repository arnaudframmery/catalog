from DB.tables import Component, Catalog
from service.helper import object_as_dict


def get_sortable_components_service(session, catalog_id):
    result = session\
        .query(Component.label, Component.id)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .filter(Component.is_sortable)\
        .all()
    return object_as_dict(result)
