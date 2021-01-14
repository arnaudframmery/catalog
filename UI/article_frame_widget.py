from PyQt5 import QtWidgets, QtCore
from UI.qt_ui.article_frame_UI import Ui_Form


class ArticleFrameWidget(QtWidgets.QWidget, Ui_Form):
    articleClickedOn = QtCore.pyqtSignal(int, str)

    def __init__(self, text, id, *args, obj=None, **kwargs):
        super(ArticleFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.text = text
        self.id = id
        self.label.setText(text)

    def mouseReleaseEvent(self, QMouseEvent):
        self.articleClickedOn.emit(self.id, self.text)
