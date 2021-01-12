from PyQt5 import QtWidgets, QtCore
from UI.qt_ui.detail_frame_UI import Ui_Form


class DetailFrameWidget(QtWidgets.QWidget, Ui_Form):
    articleClickedOn = QtCore.pyqtSignal(object)

    def __init__(self, *args, obj=None, **kwargs):
        super(DetailFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
