import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from UI.catalog_frame_widget import CatalogFrameWidget
from UI.qt_ui.main_window_UI import Ui_CatalogUI


class MainWindow(QtWidgets.QMainWindow, Ui_CatalogUI):

    def __init__(self, controler, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.controler = controler

        self.catalog_tab_widget = QtWidgets.QTabWidget()
        self.catalog_tabs = []
        self.articles = []

        self.init_UI()
        if self.catalog_tabs:
            self.catalog_tab_widget.setCurrentIndex(0)
            self.display_articles(self.catalog_tabs[0]['id'], self.catalog_tab_widget.currentIndex())

        self.set_connections()

        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.catalog_tab_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def init_UI(self):
        catalogs = self.controler.get_catalogs()
        for tab in catalogs:
            self.catalog_tabs.append({'widget': CatalogFrameWidget(), 'id': tab['id']})
            self.catalog_tab_widget.addTab(self.catalog_tabs[-1]['widget'], tab['name'])

    def set_connections(self):
        self.catalog_tab_widget.currentChanged.connect(
            lambda index: self.display_articles(self.catalog_tabs[index]['id'], index)
        )

    def display_articles(self, catalog_id, tab_index):
        self.articles = []
        articles = self.controler.get_articles(catalog_id)
        articles_layout = QVBoxLayout()
        for an_article in articles:
            label = QtWidgets.QLabel(an_article['title'])
            self.articles.append({'widget': label, 'id': an_article['id']})
            articles_layout.addWidget(label)
        articles_layout.addStretch()
        self.catalog_tabs[tab_index]['widget'].scrollArea.setLayout(articles_layout)


def launch_UI(controler):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(controler)
    window.show()
    app.exec()
