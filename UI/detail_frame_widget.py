from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFormLayout, QLabel, QWidget
from UI.qt_ui.detail_frame_UI import Ui_Form


class DetailFrameWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self, title, detail,  *args, obj=None, **kwargs):
        super(DetailFrameWidget, self).__init__(*args, **kwargs)
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
