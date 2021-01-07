from PyQt5 import QtWidgets
from UI.qt_ui.catalog_frame_UI import Ui_Form


class CatalogFrameWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self, *args, obj=None, **kwargs):
        super(CatalogFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
