from DB.tables import Catalog


def get_catalogs_service(session):
    return session.query(Catalog.id, Catalog.name).all()
