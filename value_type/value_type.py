

class ValueType:
    """
    Manage the value type of a component
    """

    @staticmethod
    def check_consistency(value):
        """check if the value is compatible with the value type"""
        raise NotImplementedError

    @staticmethod
    def recovery_process(value):
        """try to process a value into the value type (None if impossible)"""
        raise NotImplementedError

    @staticmethod
    def create_edit_widget(value):
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
