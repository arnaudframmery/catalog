from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from constant import TW_BORDER_WIDTH, TW_COLOR_BACKGROUND, TW_RADIUS, TW_COLOR_BORDER, TW_COLOR_BACKGROUND_TAB, \
    TW_RADIUS_TAB, TW_COLOR_TEXT_TAB, TW_COLOR_TEXT_TAB_HOVER, TW_COLOR_BACKGROUND_TAB_SELECTED, \
    TW_COLOR_TEXT_TAB_SELECTED, TW_MARGIN, TW_PADDING, TW_FONT_SIZE


class TabWidget(QtWidgets.QTabWidget):

    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)
        font = QFont('Arial', TW_FONT_SIZE)
        font.setBold(True)
        self.tabBar().setFont(font)

        self.setStyleSheet(
            "QTabWidget::pane {"
            f"  border: {TW_BORDER_WIDTH}px solid rgb{TW_COLOR_BORDER};"
            f"  border-bottom-left-radius: {TW_RADIUS}px;"
            f"  border-bottom-right-radius: {TW_RADIUS}px;"
            f"  border-top-right-radius: {TW_RADIUS}px;"
            f"  top: {-1}px;"
            f"  margins: {TW_MARGIN}px;"
            f"  background: rgb{TW_COLOR_BACKGROUND};"
            "}"
            "QTabBar::tab {"
            f"  background: rgb{TW_COLOR_BACKGROUND_TAB};"
            f"  border: {TW_BORDER_WIDTH}px solid rgb{TW_COLOR_BORDER};"
            f"  border-bottom: {0}px solid;"
            f"  border-top-left-radius: {TW_RADIUS_TAB}px;"
            f"  border-top-right-radius: {TW_RADIUS_TAB}px;"
            f"  padding: {'px '.join(map(str, TW_PADDING)) + 'px'};"
            "}"
            "QTabBar::tab:!selected {"
            f"  border-bottom: {TW_BORDER_WIDTH}px solid rgb{TW_COLOR_BORDER};"
            f"  color: rgb{TW_COLOR_TEXT_TAB};"
            "}"
            "QTabBar::tab:hover {"
            f"  border-bottom: {TW_BORDER_WIDTH}px solid rgb{TW_COLOR_BORDER};"
            f"  color: rgb{TW_COLOR_TEXT_TAB_HOVER};"
            "}"
            "QTabBar::tab:selected {"
            f"  background: rgb{TW_COLOR_BACKGROUND_TAB_SELECTED};"
            f"  border-bottom: {0}px solid;"
            f"  color: rgb{TW_COLOR_TEXT_TAB_SELECTED};"
            "}"
            ""
            "QTabBar::tab:selected {"
            f"  margin-left: {-2}px;"
            f"  margin-right: {-2}px;"
            "}"
            "QTabBar::tab:!selected {"
            f"  margin-top: {2}px;"
            "}"
            "QTabBar::tab:first:selected {"
            f"  margin-left: {0};"
            "}"
            "QTabBar::tab:last:selected {"
            f"  margin-right: {0};"
            "}"
            "QTabBar::tab:only-one {"
            f"  margin: {0};"
            "}"
        )
