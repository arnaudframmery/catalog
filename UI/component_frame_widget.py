from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from UI.qt_ui.component_frame_UI import Ui_Form
from constant import VALUE_TYPE_MAPPING, DEFAULT_FILTER_CODE


class ComponentFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of component settings
    """

    deleteReleased = QtCore.pyqtSignal(object)

    def __init__(self, id, label, is_sortable, default_value, filter_code, type_code, filter_list, type_list, *args, obj=None, **kwargs):
        super(ComponentFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.id = id
        self.label = label
        self.is_sortable = is_sortable
        self.default_value = default_value
        self.filter_code = filter_code
        self.type_code = type_code
        self.filter_list = [a_filter['code'] for a_filter in filter_list]
        self.type_list = [a_type['code'] for a_type in type_list]
        self.value_type_class = VALUE_TYPE_MAPPING[self.type_code]

        self.init_UI()

        self.delete_button.released.connect(lambda: self.deleteReleased.emit(self))
        self.value_type_combo_box.currentTextChanged.connect(self.on_value_type_combo_box_change)

    def init_UI(self):
        """create the component settings display"""
        self.name_line_edit.setText(self.label)

        self.filter_combo_box.insertItems(0, self.filter_list)
        self.filter_combo_box.setCurrentIndex(self.filter_list.index(self.filter_code))
        self.filter_combo_box.setEnabled(self.value_type_class.is_filterable())

        self.value_type_combo_box.insertItems(0, self.type_list)
        self.value_type_combo_box.setCurrentIndex(self.type_list.index(self.type_code))

        if self.is_sortable:
            self.sorting_check_box.setCheckState(Qt.Checked)
        self.sorting_check_box.setEnabled(self.value_type_class.is_sortable())

        self.replace_default_value_widget(self.default_value, self.type_code)

    def is_new(self):
        """is this component a new one"""
        return self.id is None

    def get_data(self):
        """recover component data that the user has given"""
        default_value_text = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        filter_code = (
            self.filter_combo_box.currentText()
            if self.value_type_class.is_filterable()
            else DEFAULT_FILTER_CODE
        )
        return {
            'id': self.id,
            'label': self.name_line_edit.text(),
            'is_sortable': self.value_type_class.is_sortable() and self.sorting_check_box.checkState() == Qt.Checked,
            'default_value': default_value_text,
            'filter_code': filter_code,
            'type_code': self.value_type_combo_box.currentText(),
            'previous_type_code': self.type_code,
        }

    def has_changed(self):
        """has this component changed"""
        default_value_text = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        return ((self.label != self.name_line_edit.text()) or
                (self.is_sortable != (self.sorting_check_box.checkState() == Qt.Checked)) or
                (self.default_value != default_value_text) or
                (self.filter_code != self.filter_combo_box.currentText()) or
                (self.type_code != self.value_type_combo_box.currentText()))

    def get_id(self):
        """recover the component id"""
        return self.id

    def is_filled(self):
        """check if all necessary fields are filled"""
        return (self.name_line_edit.text().replace(' ', '') != '' and
                self.value_type_class.is_filled(self.default_line_edit))

    def replace_default_value_widget(self, old_default_value, old_code):
        """replace de default value widget with the value type edit widget"""
        self.default_line_edit.setVisible(False)
        self.default_line_edit.destroy()

        if self.value_type_class.is_recovery_accepted(old_code):
            self.default_line_edit = self.value_type_class.create_edit_widget(old_default_value)
        else:
            self.default_line_edit = self.value_type_class.create_edit_widget(None)

        self.gridLayout.addWidget(self.default_line_edit, 1, 1, 1, 1)

    def on_value_type_combo_box_change(self, code):
        """actions to do when the value type is changed"""
        old_default_value = self.value_type_class.get_edit_widget_data(self.default_line_edit)
        old_code = self.value_type_class.get_code()
        self.value_type_class = VALUE_TYPE_MAPPING[code]

        self.filter_combo_box.setEnabled(self.value_type_class.is_filterable())
        self.sorting_check_box.setEnabled(self.value_type_class.is_sortable())

        self.replace_default_value_widget(old_default_value, old_code)
