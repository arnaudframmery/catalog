from PyQt5 import QtWidgets

from constant import BUTTON_RADIUS, BUTTON_BORDER_WIDTH, BUTTON_MARGIN, BUTTON_PADDING, BUTTON_FONT_SIZE, \
    BUTTON_COLOR_BACKGROUND, BUTTON_COLOR_BACKGROUND_HOVER, BUTTON_COLOR_BACKGROUND_PRESSED, BUTTON_COLOR_TEXT, \
    BUTTON_COLOR_TEXT_HOVER, BUTTON_COLOR_TEXT_PRESSED, BUTTON_COLOR_BACKGROUND_DISABLED, BUTTON_COLOR_TEXT_DISABLED, \
    BUTTON_COLOR_BORDER_ENABLED, BUTTON_COLOR_BORDER_DISABLED


class DialogButtonBox(QtWidgets.QDialogButtonBox):
    """
    A QDialogButtonBox where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        style = kwargs.pop('style') if 'style' in kwargs else 1
        super(DialogButtonBox, self).__init__(*args, **kwargs)

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
