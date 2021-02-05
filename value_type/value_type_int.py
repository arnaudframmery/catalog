import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit

from value_type.value_type import ValueType


class ValueTypeInt(ValueType):
    """
    an int
    """

    @staticmethod
    def check_consistency(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def recovery_process(value):
        if ValueTypeInt.check_consistency(value):
            return str(int(value))
        else:
            return None

    @staticmethod
    def create_edit_widget(value):
        widget = QLineEdit()
        widget.setValidator(QRegExpValidator(QRegExp(r'[+\-\d][\d]+')))
        value = ValueTypeInt.recovery_process(value)
        if value:
            widget.setText(value)
        return widget

    @staticmethod
    def is_filled(widget):
        return re.search(r'^[+\-\d]*[\d]+$', widget.text()) is not None

    @staticmethod
    def get_edit_widget_data(widget):
        return ValueTypeInt.recovery_process(widget.text())
