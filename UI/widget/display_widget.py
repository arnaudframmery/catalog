from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPalette, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSizePolicy

from constant import DW_PAINT_WIDTH, DW_SPACING, DW_MARGIN, DW_RADIUS, DW_PAINT_LINE_GAP, DW_COLOR_DARK, DW_COLOR_LIGHT, \
    DW_TITLE_FONT_SIZE


class QDisplayWidget(QtWidgets.QWidget):
    """
    Manage the display of a component data
    """

    def __init__(self, title, widget, dev=False, *args, **kwargs):
        super(QDisplayWidget, self).__init__(*args, **kwargs)
        self.width = DW_PAINT_WIDTH
        self.spacing = DW_SPACING
        self.margin = DW_MARGIN
        self.color_dark_rgb = DW_COLOR_DARK
        self.color_light_rgb = DW_COLOR_LIGHT
        self.color_dark = QtGui.QColor(*self.color_dark_rgb)
        self.color_light = QtGui.QColor(*self.color_light_rgb)
        self.radius = DW_RADIUS
        self.line_gap = DW_PAINT_LINE_GAP
        self.title_font_size = DW_TITLE_FONT_SIZE

        self.layout = QVBoxLayout()
        self.layout.setSpacing(self.spacing)
        self.layout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        self.setLayout(self.layout)

        self.widget = widget
        self.widget.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.widget.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        self.widget.setMouseTracking(True)

        font_title = QFont('Arial', self.title_font_size)
        font_title.setBold(True)

        self.title_widget = QLabel(title)
        self.title_widget.setSizePolicy(QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))
        self.title_widget.setFont(font_title)
        self.title_widget.setStyleSheet(f"color: rgb{self.color_light_rgb};")
        self.title_widget.setMouseTracking(True)

        self.layout.addWidget(self.title_widget)
        self.layout.addWidget(widget)

        if dev:
            palette = QtGui.QPalette()
            palette.setColor(QPalette.Background, QtGui.QColor(200, 200, 200))
            self.widget.setPalette(palette)
            self.widget.setAutoFillBackground(True)
            self.title_widget.setPalette(palette)
            self.title_widget.setAutoFillBackground(True)

    def get_widget(self):
        """Return the displayed widget"""
        return self.widget

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
        painter.setPen(pen_light)
        painter.drawLine(self.width + self.line_gap,
                         self.margin + self.title_widget.rect().height() + self.spacing // 2,
                         self.rect().width() - self.width - self.line_gap,
                         self.margin + self.title_widget.rect().height() + self.spacing // 2)
