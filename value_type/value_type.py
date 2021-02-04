

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
