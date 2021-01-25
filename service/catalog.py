from DB.tables import Catalog
from service.helper import object_as_dict


def get_catalogs_service(session):
    """recover all the catalogs"""
    result = session\
        .query(Catalog.id, Catalog.name)\
        .all()
    return object_as_dict(result)


def create_catalog_service(session, catalog_name):
    """create a new catalog"""
    new_catalog = Catalog(name=catalog_name, theme='base')
    session.add(new_catalog)
    session.commit()
    return new_catalog.id


def delete_catalog_service(session, catalog_id):
    """delete a specific catalog"""
    catalog = session\
        .query(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .one()
    session.delete(catalog)
    session.commit()
