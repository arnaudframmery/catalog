from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from constant import COMBO_BOX_COLOR_BACKGROUND, COMBO_BOX_COLOR_BACKGROUND_HOVER, COMBO_BOX_COLOR_BACKGROUND_SELECTED, \
    COMBO_BOX_COLOR_TEXT, COMBO_BOX_COLOR_TEXT_SELECTED, COMBO_BOX_COLOR_BORDER, COMBO_BOX_RADIUS, \
    COMBO_BOX_BORDER_WIDTH, COMBO_BOX_PADDING_RIGHT_ARROW, COMBO_BOX_FONT_SIZE, COMBO_BOX_PADDING, \
    COMBO_BOX_COLOR_BACKGROUND_DISABLED, COMBO_BOX_COLOR_TEXT_DISABLED, COMBO_BOX_COLOR_BORDER_DISABLED


class ComboBox(QtWidgets.QComboBox):
    """
    A QComboBox where the style can be easily changed
    """

    def __init__(self, *args, **kwargs):
        super(ComboBox, self).__init__(*args, **kwargs)

        self.background_color = COMBO_BOX_COLOR_BACKGROUND
        self.background_color_hover = COMBO_BOX_COLOR_BACKGROUND_HOVER
        self.background_color_selected = COMBO_BOX_COLOR_BACKGROUND_SELECTED
        self.background_color_disabled = COMBO_BOX_COLOR_BACKGROUND_DISABLED
        self.text_color = COMBO_BOX_COLOR_TEXT
        self.text_color_selected = COMBO_BOX_COLOR_TEXT_SELECTED
        self.text_color_disabled = COMBO_BOX_COLOR_TEXT_DISABLED
        self.border_color = COMBO_BOX_COLOR_BORDER
        self.border_color_disabled = COMBO_BOX_COLOR_BORDER_DISABLED

        self.radius = COMBO_BOX_RADIUS
        self.border_width = COMBO_BOX_BORDER_WIDTH
        self.arrow_right_padding = COMBO_BOX_PADDING_RIGHT_ARROW
        self.font_size = COMBO_BOX_FONT_SIZE
        self.padding = COMBO_BOX_PADDING

        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.setFont(font)

        self.setStyleSheet(
            "QComboBox {"
            f"  border: {self.border_width}px solid rgb{self.border_color};"
            f"  border-radius: {self.radius}px;"
            f"  color: rgb{self.text_color};"
            f"  background-color: rgb{self.background_color};"
            f"  padding: {'px '.join(map(str, self.padding)) + 'px'};"
            "}"
            "QComboBox QAbstractItemView {"
            f"   border: {self.border_width}px solid rgb{self.border_color};"
            f"   background-color: rgb{self.background_color};"
            f"   selection-background-color: rgb{self.background_color_selected};"
            f"   selection-color: rgb{self.text_color_selected};"
            f"   outline: 0px;"
            "}"
            "QComboBox:hover {"
            f"   background-color: rgb{self.background_color_hover};"
            "}"
            "QComboBox:drop-down {"
            f"   border-radius: {self.radius}px;"
            f"   right: {self.arrow_right_padding}px;"
            "}"
            "QComboBox::down-arrow {"
            f"   image: url(UI/icons/arrow_down_black.png);"
            "}"
            "QComboBox::down-arrow:on {"
            f"   image: url(UI/icons/arrow_up_black.png);"
            "}"
            "QComboBox::down-arrow:disabled {"
            f"  image: url(UI/icons/arrow_down_grey.png);"
            "}"
            "QComboBox:disabled {"
            f"  background-color: rgb{self.background_color_disabled};"
            f"  color: rgb{self.text_color_disabled};"
            f"  border: {self.border_width}px solid rgb{self.border_color_disabled};"
            "}"
        )
