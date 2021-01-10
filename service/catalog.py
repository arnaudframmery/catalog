from DB.tables import Catalog
from service.helper import object_as_dict


def get_catalogs_service(session):
    return object_as_dict(session.query(Catalog.id, Catalog.name).all())
