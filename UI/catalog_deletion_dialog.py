from PyQt5 import QtWidgets
from UI.qt_ui.catalog_deletion_UI import Ui_Dialog


class CatalogDeletionDialog(QtWidgets.QDialog, Ui_Dialog):
    """
    Manage the deletion of a specific catalog by the user
    """

    def __init__(self, parent, catalog_name, *args, obj=None, **kwargs):
        super(CatalogDeletionDialog, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.label.setText(f'Are you sure you want to delete the catalog {catalog_name} ?')
