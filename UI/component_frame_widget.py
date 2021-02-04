from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from UI.qt_ui.component_frame_UI import Ui_Form
from constant import VALUE_TYPE_MAPPING


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
        self.delete_button.released.connect(lambda: self.deleteReleased.emit(self))

        self.init_UI()

    def init_UI(self):
        """create the component settings display"""
        self.name_line_edit.setText(self.label)
        self.default_line_edit.setText(self.default_value)
        self.filter_combo_box.insertItems(0, self.filter_list)
        self.filter_combo_box.setCurrentIndex(self.filter_list.index(self.filter_code))
        self.value_type_combo_box.insertItems(0, self.type_list)
        self.value_type_combo_box.setCurrentIndex(self.type_list.index(self.type_code))
        if self.is_sortable:
            self.sorting_check_box.setCheckState(Qt.Checked)

    def is_new(self):
        """is this component a new one"""
        return self.id is None

    def get_data(self):
        """recover component data that the user has given"""
        # tmp = VALUE_TYPE_MAPPING[self.value_type_combo_box.currentText()].recovery_process
        return {
            'id': self.id,
            'label': self.name_line_edit.text(),
            'is_sortable': self.sorting_check_box.checkState() == Qt.Checked,
            'default_value': self.default_line_edit.text(),
            'filter_code': self.filter_combo_box.currentText(),
            'type_code': self.value_type_combo_box.currentText(),
            'previous_type_code': self.type_code,
        }

    def has_changed(self):
        """has this component changed"""
        return ((self.label != self.name_line_edit.text()) or
                (self.is_sortable != (self.sorting_check_box.checkState() == Qt.Checked)) or
                (self.default_value != self.default_line_edit.text()) or
                (self.filter_code != self.filter_combo_box.currentText()) or
                (self.type_code != self.value_type_combo_box.currentText()))

    def get_id(self):
        """recover the component id"""
        return self.id

    def is_filled(self):
        """check if all necessary fields are filled"""
        return (self.name_line_edit.text().replace(' ', '') != '' and
                self.default_line_edit.text().replace(' ', '') != '')

    def is_type_matching_default(self):
        """check if the default value is coherent with the type"""
        return VALUE_TYPE_MAPPING[self.value_type_combo_box.currentText()].check_consistency(
            self.default_line_edit.text()
        )
