from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSizePolicy

from constant import BUTTON_RADIUS, BUTTON_BORDER_WIDTH, BUTTON_MARGIN, BUTTON_PADDING, BUTTON_FONT_SIZE, \
    BUTTON_COLOR_BACKGROUND, BUTTON_COLOR_BACKGROUND_HOVER, BUTTON_COLOR_BACKGROUND_PRESSED, BUTTON_COLOR_TEXT, \
    BUTTON_COLOR_TEXT_HOVER, BUTTON_COLOR_TEXT_PRESSED, BUTTON_COLOR_BACKGROUND_DISABLED, BUTTON_COLOR_TEXT_DISABLED, \
    BUTTON_COLOR_BORDER_ENABLED, BUTTON_COLOR_BORDER_DISABLED


class Button(QtWidgets.QPushButton):
    """
    A QPushButton where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        style = kwargs.pop('style') if 'style' in kwargs else 1
        icon_idle = kwargs.pop('icon_idle') if 'icon_idle' in kwargs else ''
        icon_pressed = kwargs.pop('icon_pressed') if 'icon_pressed' in kwargs else ''
        super(Button, self).__init__(*args, **kwargs)

        self.background_color = BUTTON_COLOR_BACKGROUND
        self.background_color_hover = BUTTON_COLOR_BACKGROUND_HOVER
        self.background_color_pressed = BUTTON_COLOR_BACKGROUND_PRESSED
        self.background_color_disabled = BUTTON_COLOR_BACKGROUND_DISABLED
        self.text_color = BUTTON_COLOR_TEXT
        self.text_color_hover = BUTTON_COLOR_TEXT_HOVER
        self.text_color_pressed = BUTTON_COLOR_TEXT_PRESSED
        self.text_color_disabled = BUTTON_COLOR_TEXT_DISABLED
        self.border_color_enabled = BUTTON_COLOR_BORDER_ENABLED
        self.border_color_disabled = BUTTON_COLOR_BORDER_DISABLED

        self.radius = BUTTON_RADIUS[style - 1]
        self.border_width = BUTTON_BORDER_WIDTH
        self.margin = BUTTON_MARGIN
        self.padding = BUTTON_PADDING
        self.font_size = BUTTON_FONT_SIZE

        self.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))

        if icon_idle and icon_pressed:
            self.set_icons(icon_idle, icon_pressed)

        self.init_style_sheet()

    def init_style_sheet(self):
        self.setStyleSheet(
            "QPushButton {"
            f"  font: {self.font_size}pt 'Arial';"
            f"  font-weight: bold;"
            f"  background-color: rgb{self.background_color};"
            f"  color: rgb{self.text_color};"
            f"  border-radius: {self.radius}px;"
            f"  border: {self.border_width}px solid rgb{self.border_color_enabled};"
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
            "QPushButton:disabled {"
            f"  background-color: rgb{self.background_color_disabled};"
            f"  color: rgb{self.text_color_disabled};"
            f"  border: {self.border_width}px solid rgb{self.border_color_disabled};"
            "}"
        )

    def set_icons(self, icon_idle, icon_pressed):
        self.icon_pressed = QIcon(icon_pressed)
        self.icon_idle = QIcon(icon_idle)
        self.setIcon(self.icon_idle)
        if self.isCheckable():
            self.released.connect(self.set_icon_toggle)
        else:
            self.pressed.connect(self.set_icon_pressed)
            self.released.connect(self.set_icon_idle)

    def set_icon_pressed(self):
        self.setIcon(self.icon_pressed)

    def set_icon_idle(self):
        self.setIcon(self.icon_idle)

    def set_icon_toggle(self):
        if self.isChecked():
            self.setIcon(self.icon_pressed)
        else:
            self.setIcon(self.icon_idle)
