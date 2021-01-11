from PyQt5 import QtWidgets
from UI.qt_ui.article_frame_UI import Ui_Form


class ArticleFrameWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self, text, *args, obj=None, **kwargs):
        super(ArticleFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.label.setText(text)
