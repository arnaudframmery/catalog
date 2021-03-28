from DB.tables import Catalog
from service.helper import object_as_dict


def get_catalogs_service(session):
    """recover all the catalogs"""
    result = session\
        .query(Catalog.id, Catalog.name)\
        .all()
    return object_as_dict(result)


def get_catalog_display_setting_service(session, catalog_id):
    """recover a specific catalog display setting"""
    result = session\
        .query(Catalog.row_number, Catalog.column_number)\
        .filter(Catalog.id == catalog_id)\
        .one()
    return object_as_dict(result)


def create_catalog_service(session, catalog_name):
    """create a new catalog"""
    new_catalog = Catalog(name=catalog_name, theme='base')
    session.add(new_catalog)
    session.commit()
    return new_catalog.id


def update_catalog_display_setting_service(session, catalog_id, row_number, column_number):
    """update the display settings of one component"""
    catalog = session\
        .query(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .one()
    catalog.row_number = int(row_number)
    catalog.column_number = int(column_number)
    session.commit()


def delete_catalog_service(session, catalog_id):
    """delete a specific catalog"""
    catalog = session\
        .query(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .one()
    session.delete(catalog)
    session.commit()
