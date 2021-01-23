from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from UI.qt_ui.component_frame_UI import Ui_Form


class ComponentFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of component settings
    """

    deleteReleased = QtCore.pyqtSignal(object)

    def __init__(self, id, label, is_sortable, default_value, filter_code, type_list, *args, obj=None, **kwargs):
        super(ComponentFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.id = id
        self.label = label
        self.is_sortable = is_sortable
        self.default_value = default_value
        self.filter_code = filter_code
        self.type_list = [a_type['code'] for a_type in type_list]
        self.delete_button.released.connect(lambda: self.deleteReleased.emit(self))

        self.init_UI()

    def init_UI(self):
        """create the component settings display"""
        self.name_line_edit.setText(self.label)
        self.default_line_edit.setText(self.default_value)
        self.filter_combo_box.insertItems(0, self.type_list)
        self.filter_combo_box.setCurrentIndex(self.type_list.index(self.filter_code))
        if self.is_sortable:
            self.sorting_check_box.setCheckState(Qt.Checked)

    def is_new(self):
        """is this component a new one"""
        return self.id is None

    def get_data(self):
        """recover component data that the user has given"""
        return {
            'id': self.id,
            'label': self.name_line_edit.text(),
            'is_sortable': self.sorting_check_box.checkState() == Qt.Checked,
            'default_value': self.default_line_edit.text(),
            'filter_code': self.filter_combo_box.currentText(),
        }

    def has_changed(self):
        """has this component changed"""
        return ((self.label != self.name_line_edit.text()) or
                (self.is_sortable != (self.sorting_check_box.checkState() == Qt.Checked)) or
                (self.default_value != self.default_line_edit.text()) or
                (self.filter_code != self.filter_combo_box.currentText()))

    def get_id(self):
        """recover the component id"""
        return self.id

