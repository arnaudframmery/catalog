import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from UI.catalog_frame_widget import CatalogFrameWidget
from UI.qt_ui.main_window_UI import Ui_CatalogUI


class MainWindow(QtWidgets.QMainWindow, Ui_CatalogUI):

    def __init__(self, controler, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.controler = controler

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
        catalogs = self.controler.get_catalogs()
        for tab in catalogs:
            catalog_frame = CatalogFrameWidget(self.controler, tab['id'])
            self.catalog_tabs.append(catalog_frame)
            self.catalog_tab_widget.addTab(catalog_frame, tab['name'])

    def set_connections(self):
        self.catalog_tab_widget.currentChanged.connect(
            self.on_tab_change
        )

    def on_tab_change(self, index):
        self.catalog_tabs[index].on_focus()


def launch_UI(controler):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(controler)
    window.show()
    app.exec()
