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
