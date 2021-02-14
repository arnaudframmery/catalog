from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFormLayout, QWidget
from UI.qt_ui.detail_frame_UI import Ui_Form
from constant import VALUE_TYPE_MAPPING


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
        self.is_updated = False
        self.setupUi(self)
        self.state = 'READ'

        self.label.setText(self.title)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setVisible(False)
        self.line_edit_label.setEnabled(False)
        self.line_edit_label.setVisible(False)
        if not self.article_id:
            self.delete_button.setEnabled(False)
            self.delete_button.setVisible(False)
            self.return_button.setEnabled(False)
            self.return_button.setVisible(False)

        self.layout = QFormLayout()
        self.layout_widget = QWidget()
        self.detail = self.controller.get_article_detail(self.article_id, self.catalog_id)
        if self.article_id:
            self.display_read_view()
        else:
            self.change_state()
        self.layout_widget.setLayout(self.layout)
        self.verticalLayout.addWidget(self.layout_widget)
        self.verticalLayout.addStretch()

        self.modify_button.released.connect(self.on_modify_release)
        self.cancel_button.released.connect(self.on_cancel_release)
        self.delete_button.released.connect(self.on_delete_release)
        self.return_button.released.connect(self.on_return_release)

    def on_modify_release(self):
        """actions to do when modify/apply button is released"""
        if self.state == 'READ':
            self.change_state()
        elif self.is_filled():
            self.create_update_article()
            self.create_update_value()
            self.change_state()

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

    def display_read_view(self):
        """display the article view where no edition is possible"""
        self.clean_frame()
        for component in self.detail:
            widget = VALUE_TYPE_MAPPING[component['code']].create_view_widget(component['value'])
            self.layout.addRow(component['label'] + ':', widget)

    def display_edit_view(self):
        """display the article view where edition is possible"""
        self.clean_frame()
        self.line_edit_label.setText(self.title)
        for a_component in self.detail:
            widget = VALUE_TYPE_MAPPING[a_component['code']].create_edit_widget(a_component['value'])
            self.layout.addRow(a_component['label'] + ':', widget)
            self.edit_widgets.append(widget)

    def clean_frame(self):
        """clean the article detail view from all the components and values"""
        for _ in range(len(self.detail)):
            self.layout.removeRow(0)
        self.edit_widgets = []

    def is_filled(self):
        """check if all necessary fields are filled"""
        condition = True
        for a_widget, a_component in zip(self.edit_widgets, self.detail):
            condition = condition and VALUE_TYPE_MAPPING[a_component['code']].is_filled(a_widget)
        return condition and self.line_edit_label.text().replace(' ', '') != ''

    def create_update_value(self):
        """create or update the values of the different components of this article"""
        to_create = []
        to_update = []
        for a_component, a_widget in zip(self.detail, self.edit_widgets):
            value = VALUE_TYPE_MAPPING[a_component['code']].get_edit_widget_data(a_widget)
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
            self.line_edit_label.setVisible(True)
            self.line_edit_label.setEnabled(True)
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
            self.label.setVisible(True)
            self.display_read_view()
