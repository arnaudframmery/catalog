from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from UI.qt_ui.catalog_creation_UI import Ui_Dialog
from constant import CATALOG_NAME_MAX_LENGTH, DIALOG_FONT_SIZE


class CatalogCreationDialog(QtWidgets.QDialog, Ui_Dialog):
    """
    Manage the creation of a new catalog by the user
    """

    def __init__(self, *args, obj=None, **kwargs):
        super(CatalogCreationDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.line_edit.setMaxLength(CATALOG_NAME_MAX_LENGTH)
        self.button_box.accepted.disconnect()
        self.button_box.accepted.connect(self.on_accept_trigger)

        font = QFont('Arial', DIALOG_FONT_SIZE)
        font.setBold(True)
        self.label.setFont(font)
        self.line_edit.setFont(font)

    def get_catalog_name(self):
        """recover the catalog name enter by the user"""
        return self.line_edit.text()

    def on_accept_trigger(self):
        """action to do when accept button is triggered"""
        if len(self.get_catalog_name()) > 0:
            self.accept()
