# Icons from Freepik
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPainter, QPen, QFont, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QWidget

from UI.widget.button import Button
from constant import EW_COLOR_DARK, EW_COLOR_LIGHT, EW_PAINT_WIDTH, EW_SPACING, EW_MARGIN, EW_RADIUS, EW_PAINT_LINE_GAP, \
    EW_TITLE_FONT_SIZE, EW_ICON_SIZE, EW_BUTTON_STYLE


class QExtendWidget(QtWidgets.QWidget):
    """
    Manage the display of a widget that can be hidden or shown
    """

    def __init__(self, title, widget, *args, **kwargs):
        super(QExtendWidget, self).__init__(*args, **kwargs)

        self.color_dark_rgb = EW_COLOR_DARK
        self.color_light_rgb = EW_COLOR_LIGHT
        self.color_dark = QtGui.QColor(*self.color_dark_rgb)
        self.color_light = QtGui.QColor(*self.color_light_rgb)

        self.width = EW_PAINT_WIDTH
        self.spacing = EW_SPACING
        self.margin = EW_MARGIN
        self.radius = EW_RADIUS
        self.line_gap = EW_PAINT_LINE_GAP
        self.font_size = EW_TITLE_FONT_SIZE
        self.icon_size = EW_ICON_SIZE
        self.button_style = EW_BUTTON_STYLE

        self.icon_arrow_down_black = QIcon('UI/icons/arrow_down_black.png')
        self.icon_arrow_down_white = QIcon('UI/icons/arrow_down_white.png')

        self.layout = QVBoxLayout()
        self.layout.setSpacing(self.spacing)
        self.layout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        self.setLayout(self.layout)

        self.widget = widget
        self.widget.setVisible(False)

        self.title_widget = QLabel(title)
        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.title_widget.setFont(font)
        self.title_widget.setStyleSheet(f"color: rgb{self.color_light_rgb};")

        self.button_extend = Button(style=self.button_style)
        self.button_extend.setIcon(self.icon_arrow_down_black)
        self.button_extend.setIconSize(QSize(self.icon_size, self.icon_size))
        self.button_extend.setCheckable(True)
        self.button_extend.toggled.connect(self.extend)

        self.layout_head = QHBoxLayout()
        self.layout_head.addWidget(self.title_widget)
        self.layout_head.addStretch()
        self.layout_head.addWidget(self.button_extend)
        self.layout_head.setContentsMargins(0, 0, 0, 0)

        self.widget_head = QWidget()
        self.widget_head.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))
        self.widget_head.setLayout(self.layout_head)

        self.layout.addWidget(self.widget_head)
        self.layout.addWidget(widget)

    def extend(self, state):
        """Hide or show the widget"""
        if not state:
            self.widget.setVisible(False)
            self.button_extend.setIcon(self.icon_arrow_down_black)
        else:
            self.widget.setVisible(True)
            self.button_extend.setIcon(self.icon_arrow_down_white)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        pen_dark = QPen()
        pen_light = QPen()
        pen_dark.setColor(self.color_dark)
        pen_dark.setWidth(self.width)
        pen_light.setColor(self.color_light)
        pen_light.setWidth(self.width)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(pen_dark)
        painter.drawRoundedRect(self.width // 2,
                                self.width // 2,
                                self.rect().width() - self.width,
                                self.rect().height() - self.width,
                                self.radius,
                                self.radius)

        if self.widget.isVisible():
            painter.setPen(pen_light)
            painter.drawLine(self.width + self.line_gap,
                             self.margin + self.title_widget.rect().height() + self.spacing // 2,
                             self.rect().width() - self.width - self.line_gap,
                             self.margin + self.title_widget.rect().height() + self.spacing // 2)
