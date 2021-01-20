from DB.tables import Catalog
from service.helper import object_as_dict


def get_catalogs_service(session):
    """recover all the catalogs"""
    result = session\
        .query(Catalog.id, Catalog.name)\
        .all()
    return object_as_dict(result)
