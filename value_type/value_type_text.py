from PyQt5.QtWidgets import QLineEdit

from value_type.value_type import ValueType


class ValueTypeText(ValueType):
    """
    The default value type: just a string
    """

    @staticmethod
    def check_consistency(value):
        return isinstance(value, str)

    @staticmethod
    def recovery_process(value):
        return value

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
