from service.catalog import get_catalogs_service


class Controler:

    def __init__(self, session):
        self.session = session

    def get_catalogs(self):
        return get_catalogs_service(self.session)
