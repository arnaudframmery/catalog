from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from UI.article_frame_widget import ArticleFrameWidget
from UI.component_setting_dialog import ComponentSettingDialog
from UI.detail_frame_widget import DetailFrameWidget
from UI.qt_ui.catalog_frame_UI import Ui_Form


class CatalogFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of catalog articles and filters (in a tab)
    """

    def __init__(self, controler, catalog_id, catalog_name, *args, **kwargs):
        super(CatalogFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.stack_widget.setCurrentIndex(0)
        self.detail_layout = QVBoxLayout()
        self.detail_stack.setLayout(self.detail_layout)
        self.sort_direction.released.connect(self.on_sorting_direction_release)

        self.controler = controler
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.filters = []
        self.articles = []
        self.apply_button = None
        self.reset_button = None

        self.sorting_component = None
        self.sortable_components = []
        self.sorting_direction = 'ASC'
        self.init_sort_frame()

        self.setting_button.released.connect(self.on_component_setting_release)
        self.sort_combo_box.currentIndexChanged.connect(self.on_sorting_change)

    def init_sort_frame(self):
        """create the sorting display"""
        self.sortable_components = self.controler.get_sortable_components(self.catalog_id)
        for i in range(self.sort_combo_box.count()):
            self.sort_combo_box.removeItem(0)
        self.sort_combo_box.insertItems(
            0,
            ['No sorting'] + [a_component['label'] for a_component in self.sortable_components]
        )

    def on_focus(self):
        """actions to do when the catalog is selected in the main window"""
        if not self.filters:
            self.display_filters()
        if not self.articles:
            self.display_articles()

    def on_apply_release(self):
        """actions to do when button 'apply' is released"""
        self.display_articles()

    def on_reset_release(self):
        """actions to do when button 'reset' is released"""
        self.display_filters()
        self.display_articles()

    def display_filters(self):
        """manage the filter area"""
        self.filters = self.controler.get_filters(self.catalog_id)
        filters_layout = QVBoxLayout()
        for a_filter in self.filters:
            a_filter.create_widget()
            filters_layout.addWidget(a_filter.get_parent_widget())
        if self.filters:
            filters_button_layout = QHBoxLayout()
            filters_button_layout_widget = QtWidgets.QWidget()
            self.apply_button = QtWidgets.QPushButton('Apply')
            self.apply_button.released.connect(self.on_apply_release)
            filters_button_layout.addWidget(self.apply_button)
            self.reset_button = QtWidgets.QPushButton('Reset')
            self.reset_button.released.connect(self.on_reset_release)
            filters_button_layout.addWidget(self.reset_button)
            filters_button_layout_widget.setLayout(filters_button_layout)
            filters_layout.addWidget(filters_button_layout_widget)
        filters_layout.addStretch()
        filters_layout_widget = QtWidgets.QWidget()
        filters_layout_widget.setLayout(filters_layout)
        self.filter_area.setWidget(filters_layout_widget)

    def display_articles(self):
        """manage the article area"""
        self.articles = []
        articles = self.controler.get_articles(
            self.catalog_id,
            self.filters,
            self.sorting_component,
            self.sorting_direction
        )
        articles_layout = QVBoxLayout()
        for an_article in articles:
            article_widget = ArticleFrameWidget(an_article['title'], an_article['id'])
            article_widget.articleClickedOn.connect(self.display_article_details)
            self.articles.append({'widget': article_widget, 'id': an_article['id']})
            articles_layout.addWidget(article_widget)
        articles_layout.addStretch()
        articles_layout_widget = QtWidgets.QWidget()
        articles_layout_widget.setLayout(articles_layout)
        self.article_area.setWidget(articles_layout_widget)

    def display_article_details(self, id, text):
        """actions to do when an article is selected"""
        detail_widget = DetailFrameWidget(self.controler, self.catalog_id, id, text)
        detail_widget.quitDetailViewSignal.connect(self.on_quit_detail_view_trigger)
        self.detail_area.setWidget(detail_widget)
        self.stack_widget.setCurrentIndex(1)

    def on_sorting_change(self, component_index):
        """actions to do when sorting component is changed"""
        if component_index == 0 or component_index == -1:
            self.sorting_component = None
            self.sort_direction.setEnabled(False)
        else:
            self.sorting_component = self.sortable_components[component_index - 1]['id']
            self.sort_direction.setEnabled(True)
        self.display_articles()

    def on_sorting_direction_release(self):
        """actions to do when sorting direction is changed"""
        if self.sorting_direction == 'ASC':
            self.sorting_direction = 'DESC'
            self.sort_direction.setText('DESC')
        elif self.sorting_direction == 'DESC':
            self.sorting_direction = 'ASC'
            self.sort_direction.setText('ASC')
        self.display_articles()

    def on_component_setting_release(self):
        """actions to do when setting button is released"""
        dialog = ComponentSettingDialog(self, self.controler, self.catalog_id)
        if dialog.exec_():
            self.display_filters()
            self.display_articles()
            self.init_sort_frame()

    def on_quit_detail_view_trigger(self, update):
        """actions to do when delete article signal is triggered"""
        self.stack_widget.setCurrentIndex(0)
        if update:
            self.display_articles()

    def get_id(self):
        """return catalog id"""
        return self.catalog_id

    def get_name(self):
        """return catalog name"""
        return self.catalog_name
