# Icons from srip, Freepik
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from UI.article_frame_widget import ArticleFrameWidget
from UI.component_setting_dialog import ComponentSettingDialog
from UI.detail_frame_widget import DetailFrameWidget
from UI.qt_ui.catalog_frame_UI import Ui_Form
from UI.widget.button import Button
from constant import SPLITTER_HANDLE_WIDTH, FA_RADIUS, AA_RADIUS, FA_COLOR_BACKGROUND, AA_COLOR_BACKGROUND, \
    SPLITTER_COLOR_HANDLE, SPLITTER_COLOR_BACKGROUND


class CatalogFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of catalog articles and filters (in a tab)
    """

    def __init__(self, controller, catalog_id, catalog_name, *args, **kwargs):
        super(CatalogFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.font_size = 9

        self.stack_widget.setCurrentIndex(0)
        self.detail_layout = QVBoxLayout()
        self.detail_stack.setLayout(self.detail_layout)
        self.splitter.setStretchFactor(0, 3)
        self.splitter.setStretchFactor(1, 7)

        self.splitter.setHandleWidth(SPLITTER_HANDLE_WIDTH)
        self.apply_splitter_style_sheet()

        self.controller = controller
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.filters = []
        self.articles = []
        self.apply_button = None
        self.reset_button = None

        self.sorting_component = None
        self.sorting_code = None
        self.sortable_components = []
        self.sorting_direction = 'ASC'
        self.init_sort_frame()

        font = QFont('Arial', self.font_size)
        font.setBold(True)
        self.sort_label.setFont(font)
        self.add_button.setLayoutDirection(Qt.LeftToRight)
        self.add_button.set_icons('UI/icons/add_black.png', 'UI/icons/add_white.png')
        self.add_button.setText(' Article')
        self.setting_button.setLayoutDirection(Qt.LeftToRight)
        self.setting_button.set_icons('UI/icons/gear_black.png', 'UI/icons/gear_white.png')
        self.setting_button.setText(' Component')
        self.sort_direction.set_icons('UI/icons/arrow_up_right_black.png', 'UI/icons/arrow_up_right_white.png')

        self.setting_button.released.connect(self.on_component_setting_release)
        self.add_button.released.connect(self.on_article_add_release)
        self.sort_direction.released.connect(self.on_sorting_direction_release)
        self.sort_combo_box.currentIndexChanged.connect(self.on_sorting_change)

    def apply_splitter_style_sheet(self):
        self.splitter.setStyleSheet(
            "QSplitter::handle{"
            f"   background-color: rgb{SPLITTER_COLOR_HANDLE};"
            "}"
            "QSplitter > QWidget{"
            f"   background-color: rgb{SPLITTER_COLOR_BACKGROUND};"
            "}"
            "#filters_layout_widget {"
            f"   background-color: rgb{FA_COLOR_BACKGROUND};"
            f"   border-radius: {FA_RADIUS};"
            "}"
            "#articles_layout_widget {"
            f"   background-color: rgb{AA_COLOR_BACKGROUND};"
            f"   border-radius: {AA_RADIUS};"
            "}"
        )

    def init_sort_frame(self):
        """create the sorting display"""
        self.sortable_components = self.controller.get_sortable_components(self.catalog_id)
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
        self.filters = self.controller.get_filters(self.catalog_id)
        filters_layout = QVBoxLayout()
        for a_filter in self.filters:
            a_filter.create_widget()
            filters_layout.addWidget(a_filter.get_parent_widget())
        if self.filters:
            filters_button_layout = QHBoxLayout()
            filters_button_layout_widget = QtWidgets.QWidget()
            self.apply_button = Button('Apply')
            self.apply_button.released.connect(self.on_apply_release)
            filters_button_layout.addWidget(self.apply_button)
            self.reset_button = Button('Reset')
            self.reset_button.released.connect(self.on_reset_release)
            filters_button_layout.addWidget(self.reset_button)
            filters_button_layout_widget.setLayout(filters_button_layout)
            filters_layout.addWidget(filters_button_layout_widget)
        filters_layout.addStretch()
        filters_layout_widget = QtWidgets.QWidget()
        filters_layout_widget.setObjectName('filters_layout_widget')
        filters_layout_widget.setLayout(filters_layout)
        self.filter_area.setWidget(filters_layout_widget)
        self.apply_splitter_style_sheet()

    def display_articles(self):
        """manage the article area"""
        self.articles = []
        articles = self.controller.get_articles(
            self.catalog_id,
            self.filters,
            self.sorting_component,
            self.sorting_direction,
            self.sorting_code,
        )
        articles_layout = QVBoxLayout()
        for an_article in articles:
            article_widget = ArticleFrameWidget(an_article['title'], an_article['id'])
            article_widget.articleClickedOn.connect(self.display_article_details)
            self.articles.append({'widget': article_widget, 'id': an_article['id']})
            articles_layout.addWidget(article_widget)
        articles_layout.addStretch()
        articles_layout_widget = QtWidgets.QWidget()
        articles_layout_widget.setObjectName('articles_layout_widget')
        articles_layout_widget.setLayout(articles_layout)
        self.article_area.setWidget(articles_layout_widget)
        self.apply_splitter_style_sheet()

    def apply_detail_widget(self, detail_widget):
        detail_widget.quitDetailViewSignal.connect(self.on_quit_detail_view_trigger)
        if not self.verticalLayout_3.isEmpty():
            widget = self.verticalLayout_3.itemAt(0).widget()
            self.verticalLayout_3.removeWidget(widget)
            widget.setVisible(False)
            widget.destroy()
        self.verticalLayout_3.addWidget(detail_widget)
        self.stack_widget.setCurrentIndex(1)

    def display_article_details(self, id, text):
        """actions to do when an article is selected"""
        detail_widget = DetailFrameWidget(self.controller, self.catalog_id, id, text)
        self.apply_detail_widget(detail_widget)

    def on_article_add_release(self):
        """actions to do when add button is released"""
        detail_widget = DetailFrameWidget(self.controller, self.catalog_id, None, '')
        self.apply_detail_widget(detail_widget)

    def on_sorting_change(self, component_index):
        """actions to do when sorting component is changed"""
        if component_index == 0 or component_index == -1:
            self.sorting_component = None
            self.sorting_code = None
            self.sort_direction.setEnabled(False)
        else:
            self.sorting_component = self.sortable_components[component_index - 1]['id']
            self.sorting_code = self.sortable_components[component_index - 1]['code']
            self.sort_direction.setEnabled(True)
        self.display_articles()

    def on_sorting_direction_release(self):
        """actions to do when sorting direction is changed"""
        if self.sorting_direction == 'ASC':
            self.sorting_direction = 'DESC'
            self.sort_direction.set_icons('UI/icons/arrow_down_right_black.png', 'UI/icons/arrow_down_right_white.png')
        elif self.sorting_direction == 'DESC':
            self.sorting_direction = 'ASC'
            self.sort_direction.set_icons('UI/icons/arrow_up_right_black.png', 'UI/icons/arrow_up_right_white.png')
        self.display_articles()

    def on_component_setting_release(self):
        """actions to do when setting button is released"""
        dialog = ComponentSettingDialog(self, self.controller, self.catalog_id)
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
