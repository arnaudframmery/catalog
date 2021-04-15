import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from UI.catalog_creation_dialog import CatalogCreationDialog
from UI.catalog_deletion_dialog import CatalogDeletionDialog
from UI.catalog_frame_widget import CatalogFrameWidget
from UI.qt_ui.main_window_UI import Ui_CatalogUI


class MainWindow(QtWidgets.QMainWindow, Ui_CatalogUI):
    """
    Manage the main window
    """

    def __init__(self, controller, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.controller = controller
        self.showMaximized()

        self.catalog_tab_widget = QtWidgets.QTabWidget()
        self.catalog_tabs = []

        self.init_UI()
        if self.catalog_tabs:
            self.catalog_tab_widget.setCurrentIndex(0)
            self.catalog_tabs[0].display_filters()
            self.catalog_tabs[0].display_articles()

        self.set_connections()

        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.catalog_tab_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def init_UI(self):
        """create the different tabs with each catalog"""
        catalogs = self.controller.get_catalogs()
        for tab in catalogs:
            catalog_frame = CatalogFrameWidget(self.controller, tab['id'], tab['name'])
            self.catalog_tabs.append(catalog_frame)
            self.catalog_tab_widget.addTab(catalog_frame, tab['name'])

    def set_connections(self):
        """set the different widget connections"""
        self.catalog_tab_widget.currentChanged.connect(self.on_tab_change)
        self.action_add_catalog.triggered.connect(self.on_add_catalog_trigger)
        self.action_remove_catalog.triggered.connect(self.on_remove_catalog_trigger)

    def on_tab_change(self, index):
        """actions to do when a tab is selected"""
        if index != -1:
            self.catalog_tabs[index].on_focus()

    def on_add_catalog_trigger(self):
        """actions to do when add catalog action is triggered"""
        dialog = CatalogCreationDialog(self)
        if dialog.exec_():
            catalog_name = dialog.get_catalog_name()
            catalog_id = self.controller.create_catalog(catalog_name)
            catalog_frame = CatalogFrameWidget(self.controller, catalog_id, catalog_name)
            self.catalog_tabs.append(catalog_frame)
            self.catalog_tab_widget.addTab(catalog_frame, catalog_name)

    def on_remove_catalog_trigger(self):
        """actions to do when remove catalog action is triggered"""
        index = self.catalog_tab_widget.currentIndex()
        name = self.catalog_tabs[index].get_name()
        catalog_id = self.catalog_tabs[index].get_id()
        dialog = CatalogDeletionDialog(self, name)
        if dialog.exec_():
            self.controller.delete_catalog(catalog_id)
            widget = self.catalog_tabs.pop(index)
            self.catalog_tab_widget.removeTab(index)
            widget.destroy()


def launch_UI(controller):
    """start the main window"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(controller)
    window.show()
    app.exec()
