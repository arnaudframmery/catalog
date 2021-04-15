import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtWidgets import QLineEdit

from constant import VALUE_TYPE_CODE, VW_FONT_SIZE
from service.value_type import sort_value_type_float_asc, sort_value_type_float_desc
from value_type.value_type import ValueType


class ValueTypeFloat(ValueType):
    """
    a float
    """

    @staticmethod
    def get_code():
        return VALUE_TYPE_CODE.FLOAT

    @staticmethod
    def check_consistency(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    @staticmethod
    def recovery_process(value):
        if ValueTypeFloat.check_consistency(value):
            return str(float(value))
        else:
            return None

    @staticmethod
    def create_edit_widget(value, style=None):
        widget = QLineEdit()
        widget.setValidator(QRegExpValidator(QRegExp(r'[+\-\d]*[\d]+[.]?[\d]*')))
        value = ValueTypeFloat.recovery_process(value)

        if value:
            widget.setText(value)

        if style is not None:
            font = QFont('Arial', VW_FONT_SIZE)
            font.setBold(True)
            widget.setFont(font)

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

    @staticmethod
    def is_recovery_accepted(code):
        if code in [VALUE_TYPE_CODE.IMAGE]:
            return False
        else:
            return True
