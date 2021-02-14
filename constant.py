from filter.filter_category import FilterCategory
from value_type.value_type_float import ValueTypeFloat
from value_type.value_type_image import ValueTypeImage
from value_type.value_type_int import ValueTypeInt
from value_type.value_type_text import ValueTypeText


FILTER_MAPPING = {
    'category': FilterCategory
}

VALUE_TYPE_MAPPING = {
    'text': ValueTypeText,
    'int': ValueTypeInt,
    'float': ValueTypeFloat,
    'image': ValueTypeImage,
}

CATALOG_NAME_MAX_LENGTH = 20

DEFAULT_FILTER_CODE = 'no filter'
DEFAULT_VALUE_TYPE_CODE = 'text'
