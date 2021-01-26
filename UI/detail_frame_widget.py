from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFormLayout, QLabel, QWidget
from UI.qt_ui.detail_frame_UI import Ui_Form


class DetailFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of article details (when an article is clicked)
    """

    deleteArticle = QtCore.pyqtSignal()

    def __init__(self, controler, article_id, title, detail,  *args, obj=None, **kwargs):
        super(DetailFrameWidget, self).__init__(*args, **kwargs)
        self.controler = controler
        self.article_id = article_id
        self.title = title
        self.detail = detail
        self.setupUi(self)

        self.label.setText(title)
        self.layout = QFormLayout()
        self.layout_widget = QWidget()
        for component in self.detail:
            self.layout.addRow(component['label'] + ':', QLabel(component['value']))

        self.layout_widget.setLayout(self.layout)
        self.verticalLayout.addWidget(self.layout_widget)
        self.verticalLayout.addStretch()

        self.modify_button.released.connect(self.on_modify_release)
        self.delete_button.released.connect(self.on_delete_release)

    def on_modify_release(self):
        print('MODIFY')

    def on_delete_release(self):
        self.controler.delete_article(self.article_id)
        self.deleteArticle.emit()
