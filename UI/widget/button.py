from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy


class Button(QtWidgets.QPushButton):
    """
    A QPushButton where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self.background_color = (214, 219, 223)
        self.background_color_hover = (174, 182, 191)
        self.background_color_pressed = (40, 55, 71)
        self.text_color = (0, 0, 0)
        self.text_color_hover = (0, 0, 0)
        self.text_color_pressed = (255, 255, 255)

        self.radius = 10
        self.border_width = 1
        self.margin = 2
        self.padding = 3
        self.font_size = 9

        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.setFont(font)
        self.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))

        self.setStyleSheet(
            "QPushButton {"
            f"  background-color: rgb{self.background_color};"
            f"  color: rgb{self.text_color};"
            f"  border-radius: {self.radius}px;"
            f"  border: {self.border_width}px solid black;"
            f"  margin: {self.margin}px;"
            f"  padding: {self.padding}px;"
            "}"
            "QPushButton:hover {"
            f"  background-color: rgb{self.background_color_hover};"
            f"  color: rgb{self.text_color_hover};"
            "}"
            "QPushButton:pressed {"
            f"  background-color: rgb{self.background_color_pressed};"
            f"  color: rgb{self.text_color_pressed};"
            "}"
            "QPushButton:checked {"
            f"  background-color: rgb{self.background_color_pressed};"
            f"  color: rgb{self.text_color_pressed};"
            "}"
        )
