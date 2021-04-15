from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy

from constant import CHECK_BOX_COLOR_BACKGROUND, CHECK_BOX_COLOR_BACKGROUND_HOVER, CHECK_BOX_COLOR_BACKGROUND_PRESSED, \
    CHECK_BOX_COLOR_TEXT, CHECK_BOX_RADIUS, CHECK_BOX_BORDER_WIDTH, CHECK_BOX_FONT_SIZE, CHECK_BOX_SIZE, \
    CHECK_BOX_COLOR_BORDER, CHECK_BOX_COLOR_BORDER_DISABLED, CHECK_BOX_COLOR_TEXT_DISABLED


class CheckBox(QtWidgets.QCheckBox):
    """
    A QCheckBox where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)

        self.background_color = CHECK_BOX_COLOR_BACKGROUND
        self.background_color_hover = CHECK_BOX_COLOR_BACKGROUND_HOVER
        self.background_color_pressed = CHECK_BOX_COLOR_BACKGROUND_PRESSED
        self.border_color = CHECK_BOX_COLOR_BORDER
        self.border_color_disabled = CHECK_BOX_COLOR_BORDER_DISABLED
        self.text_color = CHECK_BOX_COLOR_TEXT
        self.text_color_disabled = CHECK_BOX_COLOR_TEXT_DISABLED

        self.radius = CHECK_BOX_RADIUS
        self.border_width = CHECK_BOX_BORDER_WIDTH
        self.font_size = CHECK_BOX_FONT_SIZE
        self.size = CHECK_BOX_SIZE

        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.setFont(font)
        self.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))

        self.setStyleSheet(
            "QCheckBox {"
            f"  color: rgb{self.text_color};"
            "}"
            "QCheckBox:disabled {"
            f"  color: rgb{self.text_color_disabled};"
            "}"
            "QCheckBox::indicator {"
            f"  border: {self.border_width}px solid rgb{self.border_color};"
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
            "QCheckBox::indicator:disabled {"
            f"  border: {self.border_width}px solid rgb{self.border_color_disabled};"
            "}"
        )
