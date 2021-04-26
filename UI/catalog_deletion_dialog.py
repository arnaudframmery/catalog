from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from UI.qt_ui.catalog_deletion_UI import Ui_Dialog
from constant import DIALOG_FONT_SIZE


class CatalogDeletionDialog(QtWidgets.QDialog, Ui_Dialog):
    """
    Manage the deletion of a specific catalog by the user
    """

    def __init__(self, parent, catalog_name, *args, obj=None, **kwargs):
        super(CatalogDeletionDialog, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.label.setText(f'Are you sure you want to delete the catalog {catalog_name} ?')

        font = QFont('Arial', DIALOG_FONT_SIZE)
        font.setBold(True)
        self.label.setFont(font)
