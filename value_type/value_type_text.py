from PyQt5.QtWidgets import QLineEdit

from service.value_type import sort_value_type_text_asc, sort_value_type_text_desc
from value_type.value_type import ValueType


class ValueTypeText(ValueType):
    """
    The default value type: just a string
    """

    @staticmethod
    def get_code():
        return 'text'

    @staticmethod
    def check_consistency(value):
        return isinstance(value, str)

    @staticmethod
    def recovery_process(value):
        if ValueTypeText.check_consistency(value):
            return value
        else:
            return None

    @staticmethod
    def create_edit_widget(value):
        widget = QLineEdit()
        widget.setText(value)
        return widget

    @staticmethod
    def is_filled(widget):
        return widget.text().replace(' ', '') != ''

    @staticmethod
    def get_edit_widget_data(widget):
        return widget.text()

    @staticmethod
    def sort_subquery(query, subquery, direction):
        if direction == 'ASC':
            return sort_value_type_text_asc(query, subquery)
        else:
            return sort_value_type_text_desc(query, subquery)

    @staticmethod
    def is_recovery_accepted(code):
        if code in ['image']:
            return False
        else:
            return True
