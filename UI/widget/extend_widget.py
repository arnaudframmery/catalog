# Icons from Freepik
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPainter, QPen, QFont, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QWidget

from UI.widget.button import Button


class QExtendWidget(QtWidgets.QWidget):

    def __init__(self, title, widget, *args, **kwargs):
        super(QExtendWidget, self).__init__(*args, **kwargs)
        self.width = 4
        self.spacing = 16
        self.margin = 10
        self.color_dark_rgb = (40, 55, 71)
        self.color_light_rgb = (93, 109, 126)
        self.color_dark = QtGui.QColor(*self.color_dark_rgb)
        self.color_light = QtGui.QColor(*self.color_light_rgb)
        self.radius = 10.0
        self.line_gap = 5

        self.layout = QVBoxLayout()
        self.layout.setSpacing(self.spacing)
        self.layout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        self.setLayout(self.layout)

        self.widget = widget
        self.widget.setVisible(False)

        self.title_widget = QLabel(title)
        font = QFont('Arial', 11)
        font.setBold(True)
        self.title_widget.setFont(font)
        self.title_widget.setStyleSheet(f"color: rgb{self.color_light_rgb};")

        self.button_extend = Button(style=2)
        self.icon_arrow_down_black = QIcon('UI/icons/arrow_down_black.png')
        self.icon_arrow_down_white = QIcon('UI/icons/arrow_down_white.png')
        self.button_extend.setIcon(self.icon_arrow_down_black)
        self.button_extend.setIconSize(QSize(10, 10))
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
