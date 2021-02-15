from constant import VALUE_TYPE_CODE
from filter.filter_category import FilterCategory
from value_type.value_type_float import ValueTypeFloat
from value_type.value_type_image import ValueTypeImage
from value_type.value_type_int import ValueTypeInt
from value_type.value_type_text import ValueTypeText


FILTER_MAPPING = {
    'category': FilterCategory
}

VALUE_TYPE_MAPPING = {
    VALUE_TYPE_CODE.TEXT: ValueTypeText,
    VALUE_TYPE_CODE.INT: ValueTypeInt,
    VALUE_TYPE_CODE.FLOAT: ValueTypeFloat,
    VALUE_TYPE_CODE.IMAGE: ValueTypeImage,
}