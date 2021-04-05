

class VALUE_TYPE_CODE:
    TEXT = 'text'
    INT = 'int'
    FLOAT = 'float'
    IMAGE = 'image'


class FILTER_CODE:
    NO_FILTER = 'no filter'
    CATEGORY = 'category'


# Default values
DEFAULT_CODE_FILTER = FILTER_CODE.NO_FILTER
DEFAULT_CODE_VALUE_TYPE = VALUE_TYPE_CODE.TEXT
DEFAULT_COLUMN_NUMBER = 5
DEFAULT_ROW_NUMBER = 4

# Detail View
DETAIL_VIEW_SPACING = 5
DETAIL_VIEW_SPAN_HORIZONTAL = 150
DETAIL_VIEW_SPAN_VERTICAL = 100

# Color
COLOR_BLACK = (0, 0, 0)
COLOR_GREY_DARK = (40, 55, 71)
COLOR_GREY_MEDIUM = (93, 109, 126)
COLOR_GREY_QUITE_LIGHT = (133, 146, 158)
COLOR_GREY_LIGHT = (174, 182, 191)
COLOR_GREY_VERY_LIGHT = (214, 219, 223)
COLOR_WHITE = (255, 255, 255)

# Button
BUTTON_BORDER_WIDTH = 1
BUTTON_COLOR_BACKGROUND = COLOR_GREY_VERY_LIGHT
BUTTON_COLOR_BACKGROUND_DISABLED = COLOR_GREY_VERY_LIGHT
BUTTON_COLOR_BACKGROUND_HOVER = COLOR_GREY_LIGHT
BUTTON_COLOR_BACKGROUND_PRESSED = COLOR_GREY_DARK
BUTTON_COLOR_BORDER_DISABLED = COLOR_GREY_QUITE_LIGHT
BUTTON_COLOR_BORDER_ENABLED = COLOR_BLACK
BUTTON_COLOR_TEXT = COLOR_BLACK
BUTTON_COLOR_TEXT_DISABLED = COLOR_GREY_QUITE_LIGHT
BUTTON_COLOR_TEXT_HOVER = COLOR_BLACK
BUTTON_COLOR_TEXT_PRESSED = COLOR_WHITE
BUTTON_FONT_SIZE = 9
BUTTON_MARGIN = 2
BUTTON_PADDING = 4
BUTTON_RADIUS = (10, 7)

# Check Box
CHECK_BOX_BORDER_WIDTH = 2
CHECK_BOX_COLOR_BACKGROUND = COLOR_GREY_LIGHT
CHECK_BOX_COLOR_BACKGROUND_HOVER = COLOR_GREY_QUITE_LIGHT
CHECK_BOX_COLOR_BACKGROUND_PRESSED = COLOR_GREY_DARK
CHECK_BOX_COLOR_TEXT = COLOR_BLACK
CHECK_BOX_FONT_SIZE = 9
CHECK_BOX_RADIUS = 4.0
CHECK_BOX_SIZE = 10

# Combo Box
COMBO_BOX_COLOR_BACKGROUND = COLOR_GREY_VERY_LIGHT
COMBO_BOX_COLOR_BACKGROUND_HOVER = COLOR_GREY_LIGHT
COMBO_BOX_COLOR_BACKGROUND_SELECTED = COLOR_GREY_DARK
COMBO_BOX_COLOR_TEXT = COLOR_BLACK
COMBO_BOX_COLOR_TEXT_SELECTED = COLOR_WHITE
COMBO_BOX_COLOR_BORDER = COLOR_BLACK
COMBO_BOX_RADIUS = 6.0
COMBO_BOX_BORDER_WIDTH = 1
COMBO_BOX_PADDING_RIGHT_ARROW = 4
COMBO_BOX_FONT_SIZE = 9
COMBO_BOX_PADDING = (2, 18, 2, 3)

# Display Widget
DW_COLOR_DARK = COLOR_GREY_DARK
DW_COLOR_LIGHT = COLOR_GREY_MEDIUM
DW_MARGIN = 10
DW_PAINT_LINE_GAP = 5
DW_PAINT_WIDTH = 4
DW_RADIUS = 10.0
DW_SPACING = 16
DW_TITLE_FONT_SIZE = 11

# Extend Widget
EW_COLOR_DARK = COLOR_GREY_DARK
EW_COLOR_LIGHT = COLOR_GREY_MEDIUM
EW_MARGIN = 10
EW_PAINT_LINE_GAP = 5
EW_PAINT_WIDTH = 4
EW_RADIUS = 10.0
EW_SPACING = 16
EW_TITLE_FONT_SIZE = 11
EW_ICON_SIZE = 10
EW_BUTTON_STYLE = 2

# Other
CATALOG_NAME_MAX_LENGTH = 20
