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
        self.filters = []
        self.apply_button = None

        self.init_UI()
        if self.catalog_tabs:
            self.catalog_tab_widget.setCurrentIndex(0)
            self.display_filters(self.catalog_tabs[0]['id'], self.catalog_tab_widget.currentIndex())
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
            sortable_components = self.controler.get_sortable_components(tab['id'])
            explore_stack = CatalogFrameWidget(sortable_components)
            explore_stack.sort_combo_box.currentIndexChanged.connect(self.on_sorting_change)
            stack_widget = QtWidgets.QStackedWidget()
            stack_widget.addWidget(explore_stack)
            self.catalog_tabs.append({
                'explore_stack': explore_stack,
                'stack': stack_widget,
                'id': tab['id'],
                'sorting_component': None,
            })
            self.catalog_tab_widget.addTab(self.catalog_tabs[-1]['stack'], tab['name'])

    def set_connections(self):
        self.catalog_tab_widget.currentChanged.connect(
            self.on_tab_change
        )

    def on_tab_change(self, index):
        self.display_filters(self.catalog_tabs[index]['id'], index)
        self.display_articles(self.catalog_tabs[index]['id'], index)

    def on_sorting_change(self, component_index):
        index = self.catalog_tab_widget.currentIndex()
        component_id = self.catalog_tabs[index]['explore_stack'].get_sorting_component_id(component_index)
        self.catalog_tabs[index]['sorting_component'] = component_id
        print(component_id)
        self.display_articles(self.catalog_tabs[index]['id'], index)

    def on_apply_release(self):
        index = self.catalog_tab_widget.currentIndex()
        self.display_articles(self.catalog_tabs[index]['id'], index)

    def display_filters(self, catalog_id, tab_index):
        self.filters = self.controler.get_filters(catalog_id)
        filters_layout = QVBoxLayout()
        for a_filter in self.filters:
            a_filter.create_widget()
            filters_layout.addWidget(a_filter.get_parent_widget())
        if self.filters:
            self.apply_button = QtWidgets.QPushButton('Apply')
            self.apply_button.released.connect(self.on_apply_release)
            filters_layout.addWidget(self.apply_button)
        filters_layout.addStretch()
        filters_layout_widget = QtWidgets.QWidget()
        filters_layout_widget.setLayout(filters_layout)
        self.catalog_tabs[tab_index]['explore_stack'].filter_area.setWidget(filters_layout_widget)

    def display_articles(self, catalog_id, tab_index):
        self.articles = []
        sorting_component = self.catalog_tabs[tab_index]['sorting_component']
        articles = self.controler.get_articles(catalog_id, self.filters, sorting_component)
        articles_layout = QVBoxLayout()
        for an_article in articles:
            article_widget = ArticleFrameWidget(an_article['title'], an_article['id'])
            article_widget.articleClickedOn.connect(self.display_article_details)
            self.articles.append({'widget': article_widget, 'id': an_article['id']})
            articles_layout.addWidget(article_widget)
        articles_layout.addStretch()
        articles_layout_widget = QtWidgets.QWidget()
        articles_layout_widget.setLayout(articles_layout)
        self.catalog_tabs[tab_index]['explore_stack'].article_area.setWidget(articles_layout_widget)

    def display_article_details(self, id, text):
        detail = self.controler.get_article_detail(id)
        tab_index = self.catalog_tab_widget.currentIndex()
        stack_widget = self.catalog_tabs[tab_index]['stack']
        detail_stack = DetailFrameWidget(text, detail)
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
