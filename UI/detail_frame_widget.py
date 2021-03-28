from PyQt5 import QtWidgets, QtCore

from UI.widget.display_widget import QDisplayWidget
from UI.qt_ui.detail_frame_UI import Ui_Form
from constant import DETAIL_VIEW_SPAN_VERTICAL, DETAIL_VIEW_SPACING, DETAIL_VIEW_SPAN_HORIZONTAL
from mapping import VALUE_TYPE_MAPPING
from QTileLayout import QTileLayout


class DetailFrameWidget(QtWidgets.QWidget, Ui_Form):
    """
    Manage the display of article details (when an article is clicked)
    """

    quitDetailViewSignal = QtCore.pyqtSignal(bool)

    def __init__(self, controller, catalog_id, article_id, title, *args, obj=None, **kwargs):
        super(DetailFrameWidget, self).__init__(*args, **kwargs)

        self.controller = controller
        self.article_id = article_id
        self.catalog_id = catalog_id
        self.title = title
        self.edit_widgets = []
        self.widgets = []
        self.is_updated = False

        self.setupUi(self)
        self.modify_layout_button.setCheckable(True)
        self.state = 'READ'

        catalog_display_setting = self.controller.get_catalog_display_setting(self.catalog_id)
        self.row_number = catalog_display_setting['row_number']
        self.column_number = catalog_display_setting['column_number']
        self.vertical_span = DETAIL_VIEW_SPAN_VERTICAL
        self.horizontal_span = DETAIL_VIEW_SPAN_HORIZONTAL
        self.spacing = DETAIL_VIEW_SPACING

        self.label.setText(self.title)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setVisible(False)
        self.line_edit_label.setEnabled(False)
        self.line_edit_label.setVisible(False)

        if not self.article_id:
            self.delete_button.setEnabled(False)
            self.delete_button.setVisible(False)

        self.layout = QTileLayout(rowNumber=self.row_number,
                                  columnNumber=self.column_number,
                                  verticalSpan=self.vertical_span,
                                  horizontalSpan=self.horizontal_span,
                                  verticalSpacing=self.spacing,
                                  horizontalSpacing=self.spacing)
        self.layout_container = QtWidgets.QWidget()
        self.scroll = QtWidgets.QScrollArea()

        self.detail = self.controller.get_article_detail(self.article_id, self.catalog_id)
        if self.article_id:
            self.display_read_view()
        else:
            self.change_state()

        self.set_up_tile_layout()

        self.modify_button.released.connect(self.on_modify_release)
        self.modify_layout_button.toggled.connect(self.on_modify_layout_release)
        self.cancel_button.released.connect(self.on_cancel_release)
        self.delete_button.released.connect(self.on_delete_release)
        self.return_button.released.connect(self.on_return_release)

    def on_resize_trigger(self, size):
        """actions to do when the frame is resized"""
        self.layout.updateGlobalSize(size)

    def set_up_tile_layout(self):
        """set up the main layout for the detail article view"""
        self.layout_container.setContentsMargins(0, 0, 0, 0)
        self.layout_container.setLayout(self.layout)

        self.layout.acceptDragAndDrop(False)
        self.layout.acceptResizing(False)

        self.scroll.setWidgetResizable(True)
        self.scroll.setContentsMargins(0, 0, 0, 0)
        self.scroll.setWidget(self.layout_container)

        self.verticalLayout.addWidget(self.scroll)
        self.scroll.resizeEvent = self.on_resize_trigger

        vertical_margins = self.layout.contentsMargins().top() + self.layout.contentsMargins().bottom()
        horizontal_margins = self.layout.contentsMargins().left() + self.layout.contentsMargins().right()
        self.scroll.setMinimumHeight(
            self.row_number * self.vertical_span + (self.row_number - 1) * self.spacing + vertical_margins + 2
        )
        self.scroll.setMinimumWidth(
            self.column_number * self.horizontal_span + (self.column_number - 1) * self.spacing + horizontal_margins + 2
        )

        self.layout.tileResized.connect(self.on_tile_resize)
        self.layout.tileMoved.connect(self.on_tile_movement)

    def on_tile_resize(self, widget, from_row, from_column, row_span, column_span):
        """actions to do when a tile is resized"""
        component = self.detail[self.widgets.index(widget)]
        self.controller.update_component_display_setting(
            component['component_id'], from_row, from_column, row_span, column_span
        )
        component['from_row'] = from_row
        component['from_column'] = from_column
        component['row_span'] = row_span
        component['column_span'] = column_span

    def on_tile_movement(self, widget, from_row, from_column, to_row, to_column):
        """actions to do when a tile is moved"""
        component = self.detail[self.widgets.index(widget)]
        self.controller.update_component_display_setting(
            component['component_id'], to_row, to_column, component['row_span'], component['column_span']
        )
        component['from_row'] = to_row
        component['from_column'] = to_column

    def on_modify_release(self):
        """actions to do when modify/apply button is released"""
        if self.state == 'READ':
            self.change_state()
        elif self.is_filled():
            self.create_update_article()
            self.create_update_value()
            self.change_state()

    def on_modify_layout_release(self, state):
        """actions to do when modify layout button is released"""
        if state:
            self.layout.acceptDragAndDrop(True)
            self.layout.acceptResizing(True)
        else:
            self.layout.acceptDragAndDrop(False)
            self.layout.acceptResizing(False)

    def on_delete_release(self):
        """actions to do when delete button is released"""
        self.controller.delete_article(self.article_id)
        self.quitDetailViewSignal.emit(True)

    def on_cancel_release(self):
        """actions to do when cancel button is released"""
        if self.article_id:
            self.change_state()
        else:
            self.quitDetailViewSignal.emit(False)

    def on_return_release(self):
        """actions to do when return button is released"""
        self.quitDetailViewSignal.emit(self.is_updated)

    def add_widget(self, widget, component, index):
        """add a widget in the tile layout"""
        if component['from_row'] is None:
            # search for an empty space
            while not self.layout.isAreaEmpty(index // self.column_number, index % self.column_number, 1, 1):
                # if no space available -> add a row
                if ((index // self.column_number >= self.row_number - 1) and
                        (index % self.column_number >= self.column_number - 1)):
                    self.layout.addRows(1)
                    self.row_number += 1
                    self.controller.update_catalog_display_setting(self.catalog_id, self.row_number, self.column_number)
                index += 1

            self.layout.addWidget(
                widget=widget,
                fromRow=index // self.column_number,
                fromColumn=index % self.column_number,
            )
            self.controller.update_component_display_setting(
                component['component_id'],
                index // self.column_number,
                index % self.column_number,
                component['row_span'],
                component['column_span']
            )

        else:
            self.layout.addWidget(
                widget=widget,
                fromRow=component['from_row'],
                fromColumn=component['from_column'],
                rowSpan=component['row_span'],
                columnSpan=component['column_span'],
            )

        return index

    def display_read_view(self):
        """display the article view where no edition is possible"""
        self.clean_frame(self.edit_widgets)
        index = 0
        for component in self.detail:
            widget = VALUE_TYPE_MAPPING[component['code']].create_view_widget(component['value'])
            display_widget = QDisplayWidget(component['label'], widget)
            self.widgets.append(display_widget)
            index = self.add_widget(display_widget, component, index)

    def display_edit_view(self):
        """display the article view where edition is possible"""
        self.clean_frame(self.widgets)
        self.line_edit_label.setText(self.title)
        index = 0
        for component in self.detail:
            widget = VALUE_TYPE_MAPPING[component['code']].create_edit_widget(component['value'], style=True)
            display_widget = QDisplayWidget(component['label'], widget)
            self.edit_widgets.append(display_widget)
            index = self.add_widget(display_widget, component, index)

    def clean_frame(self, widgets):
        """clean the article detail view from all the components and values"""
        for a_widget in widgets:
            self.layout.removeWidget(a_widget)
        self.edit_widgets = []
        self.widgets = []

    def is_filled(self):
        """check if all necessary fields are filled"""
        condition = True
        for a_widget, a_component in zip(self.edit_widgets, self.detail):
            condition = condition and VALUE_TYPE_MAPPING[a_component['code']].is_filled(a_widget.get_widget())
        return condition and self.line_edit_label.text().replace(' ', '') != ''

    def create_update_value(self):
        """create or update the values of the different components of this article"""
        to_create = []
        to_update = []
        for a_component, a_widget in zip(self.detail, self.edit_widgets):
            value = VALUE_TYPE_MAPPING[a_component['code']].get_edit_widget_data(a_widget.get_widget())
            if a_component['value'] != value and a_component['value_id'] is None:
                to_create.append({**a_component, 'value': value, 'article_id': self.article_id})
            elif a_component['value'] != value and a_component['value_id'] is not None:
                to_update.append({**a_component, 'value': value})
        self.controller.create_values(to_create)
        self.controller.update_values(to_update)
        if to_create or to_update:
            self.is_updated = True
            self.detail = self.controller.get_article_detail(self.article_id, self.catalog_id)

    def create_update_article(self):
        """create or update the article"""
        if self.title != self.line_edit_label.text():
            if self.article_id:
                self.controller.update_article(self.article_id, self.line_edit_label.text())
            else:
                self.article_id = self.controller.create_article(self.catalog_id, self.line_edit_label.text())
                self.delete_button.setVisible(True)
                self.delete_button.setEnabled(True)
            self.title = self.line_edit_label.text()
            self.label.setText(self.title)
            self.is_updated = True

    def change_state(self):
        """switch from the read mode to the edit one, and inversely"""
        if self.state == 'READ':
            self.state = 'EDIT'
            self.modify_button.setText('Apply')
            self.label.setVisible(False)
            self.cancel_button.setVisible(True)
            self.cancel_button.setEnabled(True)
            self.modify_layout_button.setEnabled(False)
            self.modify_layout_button.setVisible(False)
            self.line_edit_label.setVisible(True)
            self.line_edit_label.setEnabled(True)
            self.modify_layout_button.setChecked(False)
            self.display_edit_view()
        else:
            self.state = 'READ'
            self.modify_button.setText('Modify')
            self.cancel_button.setEnabled(False)
            self.cancel_button.setVisible(False)
            self.line_edit_label.setEnabled(False)
            self.line_edit_label.setVisible(False)
            self.return_button.setVisible(True)
            self.return_button.setEnabled(True)
            self.modify_layout_button.setVisible(True)
            self.modify_layout_button.setEnabled(True)
            self.label.setVisible(True)
            self.display_read_view()
