# Icons from bqlqn
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

from UI.qt_ui.component_frame_UI import Ui_Form
from UI.widget.button import Button
from UI.widget.extend_widget import QExtendWidget
from UI.widget.line_edit import LineEdit
from constant import DEFAULT_CODE_FILTER, ECW_FONT_SIZE
from mapping import VALUE_TYPE_MAPPING


class QExtendComponentWidget(QExtendWidget, Ui_Form):
    """
    Manage the display of a component settings that can be hidden or shown
    """

    deleteReleased = QtCore.pyqtSignal(object)

    def __init__(self, title, id, is_sortable, default_value, filter_code, type_code, filter_list, type_list,
                 *args, **kwargs):
        self.title_edit_widget = None
        self.delete_button = None
        widget = QWidget()
        self.setupUi(widget)
        super(QExtendComponentWidget, self).__init__(title, widget, *args, **kwargs)

        self.id = id
        self.label = title
        self.is_sortable = is_sortable
        self.default_value = default_value
        self.filter_code = filter_code
        self.type_code = type_code
        self.filter_list = [a_filter['code'] for a_filter in filter_list]
        self.type_list = [a_type['code'] for a_type in type_list]
        self.value_type_class = VALUE_TYPE_MAPPING[self.type_code]

        self.init_UI()

        font = QFont('Arial', ECW_FONT_SIZE)
        font.setBold(True)
        self.default_label.setFont(font)
        self.default_line_edit.setFont(font)

        self.delete_button.released.connect(lambda: self.deleteReleased.emit(self))
        self.value_type_combo_box.currentTextChanged.connect(self.on_value_type_combo_box_change)

    def init_head(self):
        """create the head of the extend widget display"""
        self.title_widget = QLabel(self.title)
        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.title_widget.setFont(font)
        self.title_widget.setStyleSheet(f"color: rgb{self.color_light_rgb};")

        self.title_edit_widget = LineEdit(self.title)
        self.title_edit_widget.setFont(font)
        self.title_edit_widget.setVisible(False)
        self.delete_button = Button('', icon_idle='UI/icons/trash_black.png', icon_pressed='UI/icons/trash_white.png')
        self.layout_head = QHBoxLayout()
        self.layout_head.addWidget(self.title_widget)
        self.layout_head.addWidget(self.title_edit_widget)
        self.layout_head.addStretch()
        self.layout_head.addWidget(self.delete_button)
        self.layout_head.addWidget(self.button_extend)
        self.layout_head.setContentsMargins(0, 0, 0, 0)

    def init_UI(self):
        """create the component settings display"""
        self.title_edit_widget.setText(self.label)

        self.filter_combo_box.insertItems(0, self.filter_list)
        self.filter_combo_box.setCurrentIndex(self.filter_list.index(self.filter_code))
        self.filter_combo_box.setEnabled(self.value_type_class.is_filterable())

        self.value_type_combo_box.insertItems(0, self.type_list)
        self.value_type_combo_box.setCurrentIndex(self.type_list.index(self.type_code))

        if self.is_sortable:
            self.sorting_check_box.setCheckState(Qt.Checked)
        self.sorting_check_box.setEnabled(self.value_type_class.is_sortable())

        self.replace_default_value_widget(self.default_value, self.type_code)

    def extend(self, state):
        """Hide or show the widget"""
        if not state:
            self.widget.setVisible(False)
            self.button_extend.setIcon(self.icon_arrow_down_black)
            self.title_edit_widget.setVisible(False)
            self.title_widget.setVisible(True)
            self.title_widget.setText(self.title_edit_widget.text())
        else:
            self.widget.setVisible(True)
            self.button_extend.setIcon(self.icon_arrow_down_white)
            self.title_widget.setVisible(False)
            self.title_edit_widget.setVisible(True)

    def replace_default_value_widget(self, old_default_value, old_code):
        """replace de default value widget with the value type edit widget"""
        self.default_line_edit.setVisible(False)
        self.default_line_edit.destroy()

        if self.value_type_class.is_recovery_accepted(old_code):
            self.default_line_edit = self.value_type_class.create_edit_widget(old_default_value)
        else:
            self.default_line_edit = self.value_type_class.create_edit_widget(None)

        self.horizontalLayout.addWidget(self.default_line_edit)

    def is_new(self):
        """is this component a new one"""
        return self.id is None

    def get_data(self):
        """recover component data that the user has given"""
        default_value_text = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        filter_code = (
            self.filter_combo_box.currentText()
            if self.value_type_class.is_filterable()
            else DEFAULT_CODE_FILTER
        )
        return {
            'id': self.id,
            'label': self.title_edit_widget.text(),
            'is_sortable': self.value_type_class.is_sortable() and self.sorting_check_box.checkState() == Qt.Checked,
            'default_value': default_value_text,
            'filter_code': filter_code,
            'type_code': self.value_type_combo_box.currentText(),
            'previous_type_code': self.type_code,
        }

    def has_changed(self):
        """has this component changed"""
        default_value_text = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        return ((self.label != self.title_edit_widget.text()) or
                (self.is_sortable != (self.sorting_check_box.checkState() == Qt.Checked)) or
                (self.default_value != default_value_text) or
                (self.filter_code != self.filter_combo_box.currentText()) or
                (self.type_code != self.value_type_combo_box.currentText()))

    def get_id(self):
        """recover the component id"""
        return self.id

    def is_filled(self):
        """check if all necessary fields are filled"""
        return (self.title_edit_widget.text().replace(' ', '') != '' and
                self.value_type_class.is_filled(self.default_line_edit))

    def on_value_type_combo_box_change(self, code):
        """actions to do when the value type is changed"""
        old_default_value = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        old_code = self.value_type_class.get_code()
        self.value_type_class = VALUE_TYPE_MAPPING[code]

        if self.value_type_class.is_filterable():
            self.filter_combo_box.setEnabled(True)
        else:
            self.filter_combo_box.setEnabled(False)
            self.filter_combo_box.setCurrentIndex(0)

        if self.value_type_class.is_sortable():
            self.sorting_check_box.setEnabled(True)
        else:
            self.sorting_check_box.setEnabled(False)
            self.sorting_check_box.setCheckState(Qt.Unchecked)

        self.replace_default_value_widget(old_default_value, old_code)
