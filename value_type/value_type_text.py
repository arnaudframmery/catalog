from PyQt5.QtGui import QFont

from UI.widget.line_edit import LineEdit
from constant import VALUE_TYPE_CODE, VW_FONT_SIZE
from service.value_type import sort_value_type_text_asc, sort_value_type_text_desc
from value_type.value_type import ValueType


class ValueTypeText(ValueType):
    """
    The default value type: just a string
    """

    @staticmethod
    def get_code():
        return VALUE_TYPE_CODE.TEXT

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
    def create_edit_widget(value, style=None):
        widget = LineEdit()
        widget.setText(value)

        if value:
            widget.setText(value)

        if style is not None:
            font = QFont('Arial', VW_FONT_SIZE)
            font.setBold(True)
            widget.setFont(font)

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
        if code in [VALUE_TYPE_CODE.IMAGE]:
            return False
        else:
            return True
