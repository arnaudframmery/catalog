from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy

from constant import BUTTON_RADIUS, BUTTON_BORDER_WIDTH, BUTTON_MARGIN, BUTTON_PADDING, BUTTON_FONT_SIZE, \
    BUTTON_COLOR_BACKGROUND, BUTTON_COLOR_BACKGROUND_HOVER, BUTTON_COLOR_BACKGROUND_PRESSED, BUTTON_COLOR_TEXT, \
    BUTTON_COLOR_TEXT_HOVER, BUTTON_COLOR_TEXT_PRESSED


class Button(QtWidgets.QPushButton):
    """
    A QPushButton where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self.background_color = BUTTON_COLOR_BACKGROUND
        self.background_color_hover = BUTTON_COLOR_BACKGROUND_HOVER
        self.background_color_pressed = BUTTON_COLOR_BACKGROUND_PRESSED
        self.text_color = BUTTON_COLOR_TEXT
        self.text_color_hover = BUTTON_COLOR_TEXT_HOVER
        self.text_color_pressed = BUTTON_COLOR_TEXT_PRESSED

        self.radius = BUTTON_RADIUS
        self.border_width = BUTTON_BORDER_WIDTH
        self.margin = BUTTON_MARGIN
        self.padding = BUTTON_PADDING
        self.font_size = BUTTON_FONT_SIZE

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
