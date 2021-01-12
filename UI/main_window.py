import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from UI.article_frame_widget import ArticleFrameWidget
from UI.catalog_frame_widget import CatalogFrameWidget
from UI.detail_frame_widget import DetailFrameWidget
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
            explore_stack = CatalogFrameWidget()
            stack_widget = QtWidgets.QStackedWidget()
            stack_widget.addWidget(explore_stack)

            self.catalog_tabs.append({'explore_stack': explore_stack, 'stack': stack_widget, 'id': tab['id']})
            self.catalog_tab_widget.addTab(self.catalog_tabs[-1]['stack'], tab['name'])

    def set_connections(self):
        self.catalog_tab_widget.currentChanged.connect(
            lambda index: self.display_articles(self.catalog_tabs[index]['id'], index)
        )

    def display_articles(self, catalog_id, tab_index):
        self.articles = []

        articles = self.controler.get_articles(catalog_id)
        articles_layout = QVBoxLayout()
        for an_article in articles:
            article_widget = ArticleFrameWidget(an_article['title'])
            article_widget.articleClickedOn.connect(self.display_article_details)
            self.articles.append({'widget': article_widget, 'id': an_article['id']})
            articles_layout.addWidget(article_widget)
        articles_layout.addStretch()
        self.catalog_tabs[tab_index]['explore_stack'].scrollArea.setLayout(articles_layout)

    def display_article_details(self, message):
        print(message)
        tab_index = self.catalog_tab_widget.currentIndex()
        stack_widget = self.catalog_tabs[tab_index]['stack']
        detail_stack = DetailFrameWidget()
        self.catalog_tabs[tab_index]['detail_stack'] = detail_stack
        detail_stack.return_button.released.connect(self.return_to_explore_view)
        stack_widget.addWidget(detail_stack)
        stack_widget.setCurrentIndex(1)

    def return_to_explore_view(self):
        tab_index = self.catalog_tab_widget.currentIndex()
        stack_widget = self.catalog_tabs[tab_index]['stack']
        stack_widget.setCurrentIndex(0)
        stack_widget.removeWidget(self.catalog_tabs[tab_index]['detail_stack'])
        del(self.catalog_tabs[tab_index]['detail_stack'])


def launch_UI(controler):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(controler)
    window.show()
    app.exec()
