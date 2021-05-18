from typing import List

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QVBoxLayout

from UI.qt_ui.component_setting_UI import Ui_Dialog
from UI.widget.extend_component_widget import QExtendComponentWidget
from UI.widget.extend_widget import QExtendWidget

from constant import DEFAULT_CODE_FILTER, DEFAULT_CODE_VALUE_TYPE, COLOR_GREY_ULTRA_LIGHT, COLOR_WHITE, CS_RADIUS, \
    CS_COLOR_BACKGROUND


class ComponentSettingDialog(QtWidgets.QDialog, Ui_Dialog):
    """
    Manage the components settings : creation, modification, deletion
    """

    def __init__(self, parent, controller, catalog_id, *args, obj=None, **kwargs):
        super(ComponentSettingDialog, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.resize(self.rect().width(), parent.height())

        self.controller = controller
        self.catalog_id = catalog_id
        self.filters = self.controller.get_all_filters()
        self.types = self.controller.get_all_value_types()
        self.component_layout = None
        self.component_layout_widget = None
        self.components_list: List[QExtendComponentWidget] = []
        self.extend_widget_list: List[QExtendWidget] = []
        self.to_delete = []

        self.init_UI()

        self.add_button.setText(' Component')
        self.add_button.set_icons('UI/icons/add_black.png', 'UI/icons/add_white.png')
        self.component_area.set_background_color(COLOR_GREY_ULTRA_LIGHT)
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(255, 255, 255))
        self.setPalette(pal)
        self.component_layout_widget.setStyleSheet(
            "QWidget {"
            f"   background-color: rgb{CS_COLOR_BACKGROUND};"
            f"   border-radius: {0};"
            "}"
            "#component_layout_widget {"
            f"   border-radius: {CS_RADIUS};"
            "}"
        )
        self.setStyleSheet(
            "QWidget {"
            f"   background-color: rgb{COLOR_WHITE};"
            "}"
        )

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.on_reset_click)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.on_apply_click)
        self.add_button.released.connect(self.on_add_button_release)

    def init_UI(self):
        """create the components display"""
        self.components_list = []
        self.to_delete = []
        components = self.controller.get_components(self.catalog_id)
        self.component_layout = QVBoxLayout()
        self.component_layout_widget = QtWidgets.QWidget()
        self.component_layout_widget.setObjectName('component_layout_widget')
        for a_component in components:
            widget = QExtendComponentWidget(
                a_component['label'],
                a_component['id'],
                a_component['is_sortable'],
                a_component['default'],
                a_component['filter_code'],
                a_component['type_code'],
                self.filters,
                self.types,
            )
            widget.deleteReleased.connect(self.on_delete_button_release)
            self.component_layout.addWidget(widget)
            self.components_list.append(widget)
        self.component_layout.addStretch()
        self.component_layout_widget.setLayout(self.component_layout)
        self.component_area.setWidget(self.component_layout_widget)

    def on_reset_click(self, button):
        """actions to do when reset button is released"""
        self.init_UI()

    def on_add_button_release(self):
        """actions to do when add button is released"""
        widget = QExtendComponentWidget(
            '', None, False, '', DEFAULT_CODE_FILTER, DEFAULT_CODE_VALUE_TYPE, self.filters, self.types
        )
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
        self.controller.create_components(self.catalog_id, to_create)
        self.controller.update_components(to_update)
        self.controller.delete_components(self.to_delete)
        self.accept()
