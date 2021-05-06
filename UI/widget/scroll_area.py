from PyQt5 import QtWidgets, QtGui

from constant import SA_BORDER_WIDTH


class ScrollArea(QtWidgets.QScrollArea):

    def __init__(self, *args, **kwargs):
        super(ScrollArea, self).__init__(*args, **kwargs)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        """actions to do when the widget is about to be shown"""
        super().showEvent(a0)
        self.setStyleSheet(
            "QScrollArea {"
            f"   border: {SA_BORDER_WIDTH}px solid;"
            "}"
        )
