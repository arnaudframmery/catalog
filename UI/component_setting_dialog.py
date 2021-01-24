from PyQt5 import QtWidgets

from UI.component_frame_widget import ComponentFrameWidget
from UI.qt_ui.component_setting_UI import Ui_Dialog
from PyQt5.QtWidgets import QVBoxLayout


class ComponentSettingDialog(QtWidgets.QDialog, Ui_Dialog):
    """
    Manage the components settings : creation, modification, deletion
    """

    def __init__(self, parent, controler, catalog_id, *args, obj=None, **kwargs):
        super(ComponentSettingDialog, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.controler = controler
        self.catalog_id = catalog_id
        self.types = self.controler.get_all_filters()
        self.component_layout = None
        self.components_list = []
        self.to_delete = []

        self.init_UI()

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.on_reset_click)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.on_apply_click)
        self.add_button.released.connect(self.on_add_button_release)

    def init_UI(self):
        """create the components display"""
        self.components_list = []
        components = self.controler.get_components(self.catalog_id)
        self.component_layout = QVBoxLayout()
        component_layout_widget = QtWidgets.QWidget()
        for a_component in components:
            widget = ComponentFrameWidget(
                a_component['id'],
                a_component['label'],
                a_component['is_sortable'],
                a_component['default'],
                a_component['code'],
                self.types,
            )
            widget.deleteReleased.connect(self.on_delete_button_release)
            self.component_layout.addWidget(widget)
            self.components_list.append(widget)
        self.component_layout.addStretch()
        component_layout_widget.setLayout(self.component_layout)
        self.component_area.setWidget(component_layout_widget)

    def on_reset_click(self, button):
        """actions to do when reset button is released"""
        self.init_UI()

    def on_add_button_release(self):
        """actions to do when add button is released"""
        widget = ComponentFrameWidget(None, '', False, '', 'no filter', self.types)
        widget.deleteReleased.connect(self.on_delete_button_release)
        self.component_layout.insertWidget(len(self.components_list), widget)
        self.components_list.append(widget)

    def on_delete_button_release(self, widget):
        """actions to do when delete button is released"""
        index = self.components_list.index(widget)
        if widget.get_id() is not None:
            self.to_delete.append(widget.get_id())
        self.components_list.pop(index)
        self.component_layout.removeWidget(widget)
        widget.setVisible(False)
        widget.destroy()

    def on_apply_click(self):
        """actions to do when apply button is released"""
        to_create = []
        to_update = []
        for a_component in self.components_list:
            if not(a_component.is_filled()):
                return None
            if a_component.is_new():
                to_create.append(a_component.get_data())
            elif a_component.has_changed():
                to_update.append(a_component.get_data())
        self.controler.create_components(self.catalog_id, to_create)
        self.controler.update_components(to_update)
        self.controler.delete_components(self.to_delete)
        self.accept()
