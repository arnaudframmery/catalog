from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy


class CheckBox(QtWidgets.QCheckBox):

    def __init__(self, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)
        self.state = 0

        self.background_color = (174, 182, 191)
        self.background_color_hover = (133, 146, 158)
        self.background_color_pressed = (40, 55, 71)
        self.text_color = (0, 0, 0)
        self.text_color_hover = (0, 0, 0)
        self.text_color_pressed = (255, 255, 255)

        self.radius = 4
        self.border_width = 2
        self.margin = 2
        self.padding = 5
        self.font_size = 9
        self.size = 10

        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.setFont(font)
        self.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))

        self.setStyleSheet(
            "QCheckBox::indicator {"
            f"  border: {self.border_width}px solid rgb{self.background_color_pressed};"
            f"  border-radius: {self.radius}px;"
            f"  width: {self.size + 2}px;"
            f"  height: {self.size + 2}px;"
            "}"
            "QCheckBox::indicator:unchecked:hover {"
            f"  background-color: rgb{self.background_color};"
            "}"
            "QCheckBox::indicator:unchecked:pressed {"
            f"  background-color: rgb{self.background_color_hover};"
            "}"
            "QCheckBox::indicator:checked {"
            f"  border: {self.border_width + 1}px solid rgb{self.background_color_pressed};"
            f"  width: {self.size}px;"
            f"  height: {self.size}px;"
            f"  background-color: rgb{self.background_color_pressed};"
            f"  image: url(UI/icons/cross_white.png);"
            "}"
            "QCheckBox::indicator:checked:hover {"
            f"  background-color: rgb{self.background_color_pressed};"
            f"  image: url(UI/icons/cross_white.png);"
            "}"
            "QCheckBox::indicator:checked:pressed {"
            f"  background-color: rgb{self.background_color_pressed};"
            f"  image: url(UI/icons/cross_white.png);"
            "}"
        )
