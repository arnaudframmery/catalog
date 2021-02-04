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
