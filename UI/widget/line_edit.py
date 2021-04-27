from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from constant import LINE_EDIT_BORDER_WIDTH, LINE_EDIT_RADIUS, LINE_EDIT_COLOR_BACKGROUND, \
    LINE_EDIT_COLOR_BACKGROUND_SELECTION, LINE_EDIT_PADDING_VERTICAL, LINE_EDIT_PADDING_HORIZONTAL, LINE_EDIT_FONT_SIZE


class LineEdit(QtWidgets.QLineEdit):

    def __init__(self, *args, **kwargs):
        super(LineEdit, self).__init__(*args, **kwargs)
        font = QFont('Arial', LINE_EDIT_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)

        self.setStyleSheet(
            "QLineEdit {"
            f"   border: {LINE_EDIT_BORDER_WIDTH}px solid;"
            f"   border-radius: {LINE_EDIT_RADIUS}px;"
            f"   background: rgb{LINE_EDIT_COLOR_BACKGROUND};"
            f"   selection-background-color: rgb{LINE_EDIT_COLOR_BACKGROUND_SELECTION};"
            f"   padding: {LINE_EDIT_PADDING_VERTICAL} {LINE_EDIT_PADDING_HORIZONTAL}px;"
            "}"
        )
