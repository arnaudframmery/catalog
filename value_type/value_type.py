from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class ValueType:
    """
    Manage the value type of a component
    """

    @staticmethod
    def get_code():
        """return the code of this value type"""
        raise NotImplementedError

    @staticmethod
    def check_consistency(value):
        """check if the value is compatible with the value type"""
        raise NotImplementedError

    @staticmethod
    def recovery_process(value):
        """try to process a value into the value type (None if impossible)"""
        raise NotImplementedError

    @staticmethod
    def create_edit_widget(value, style=None):
        """return a widget to edit value from the current value type"""
        raise NotImplementedError

    @staticmethod
    def is_filled(widget):
        """check there is a given value"""
        raise NotImplementedError

    @staticmethod
    def get_edit_widget_data(widget):
        """get the value of the edit widget"""
        raise NotImplementedError

    @staticmethod
    def sort_subquery(query, subquery, direction):
        """sort the subquery in the correct order"""
        raise NotImplementedError

    @staticmethod
    def is_recovery_accepted(code):
        """do we recover value from this value type code ?"""
        raise NotImplementedError

    @staticmethod
    def create_view_widget(value):
        """return a widget to see value from the current value type"""
        widget = QLabel(value)
        font = QFont('Arial', 15)
        font.setBold(True)
        widget.setFont(font)
        return widget

    @staticmethod
    def is_sortable():
        """is the value type sortable ?"""
        return True

    @staticmethod
    def is_filterable():
        """is the value type filterable ?"""
        return True
