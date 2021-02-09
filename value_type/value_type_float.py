import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit

from service.value_type import sort_value_type_float_asc, sort_value_type_float_desc
from value_type.value_type import ValueType


class ValueTypeFloat(ValueType):
    """
    a float
    """

    @staticmethod
    def check_consistency(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def recovery_process(value):
        if ValueTypeFloat.check_consistency(value):
            return str(float(value))
        else:
            return None

    @staticmethod
    def create_edit_widget(value):
        widget = QLineEdit()
        widget.setValidator(QRegExpValidator(QRegExp(r'[+\-\d]*[\d]+[.]?[\d]*')))
        value = ValueTypeFloat.recovery_process(value)
        if value:
            widget.setText(value)
        return widget

    @staticmethod
    def is_filled(widget):
        return re.search(r'^[+\-\d]*[\d]+[.]?[\d]*$', widget.text()) is not None

    @staticmethod
    def get_edit_widget_data(widget):
        return ValueTypeFloat.recovery_process(widget.text())

    @staticmethod
    def sort_subquery(query, subquery, direction):
        if direction == 'ASC':
            return sort_value_type_float_asc(query, subquery)
        else:
            return sort_value_type_float_desc(query, subquery)
