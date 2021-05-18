from PyQt5 import QtWidgets, QtGui

from constant import SA_BORDER_WIDTH, SA_RADIUS, SA_WIDTH, SA_MARGIN, SA_COLOR_BACKGROUND, SA_COLOR_HANDLE


class ScrollArea(QtWidgets.QScrollArea):

    def __init__(self, *args, **kwargs):
        super(ScrollArea, self).__init__(*args, **kwargs)
        self.background_color = SA_COLOR_BACKGROUND

    def set_background_color(self, color):
        self.background_color = color

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        """actions to do when the widget is about to be shown"""
        super().showEvent(a0)
        self.setStyleSheet(
            "QScrollArea {"
            f"   border: {SA_BORDER_WIDTH}px solid;"
            "}"
            "QScrollBar {"
            f"    border: 0px solid;"
            f"    background: rgb{self.background_color};"
            f"    width: {SA_WIDTH}px;"
            f"    margin: {'px '.join(map(str, SA_MARGIN)) + 'px'};"
            "}"
            "QScrollBar::handle {"
            f"    background: rgb{SA_COLOR_HANDLE};"
            f"    min-height: 0px;"
            f"    border-radius: {SA_RADIUS}px;"
            "}"
            "QScrollBar::add-line {"
            f"    background: none;"
            f"    height: 0px;"
            f"    subcontrol-position: bottom;"
            f"    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line {"
            f"    background: none;"
            f"    height: 0px;"
            f"    subcontrol-position: top;"
            f"    subcontrol-origin: margin;"
            "}"
        )
