from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from UI.widget.check_box import CheckBox
from UI.widget.extend_widget import QExtendWidget
from filter.filter import Filter


class FilterCategory(Filter):
    """
    A filter where the user can select the articles by a specific component values.
    The categories are all the distinct values of this specific component
    """

    def __init__(self, controller, component_id, component_label):
        super().__init__(controller, component_id, component_label)
        self.categories = self.controller.get_categories(self.component_id)
        self.widgets = []

    def create_widget(self):
        layout = QVBoxLayout()
        layout_widget = QWidget()
        for a_category in self.categories:
            check_box = CheckBox(a_category)
            check_box.setCheckState(Qt.Checked)
            self.widgets.append(check_box)
            layout.addWidget(check_box)
        layout_widget.setLayout(layout)
        self.parent_widget = QExtendWidget(self.component_label, layout_widget)

    def apply_filter(self, catalog_id):
        query_categories = []
        for i in range(len(self.widgets)):
            if self.widgets[i].isChecked():
                query_categories.append(self.categories[i])
        return self.controller.apply_categories(catalog_id, self.component_id, query_categories)

    def reset_filter(self):
        for a_widget in self.widgets:
            a_widget.setCheckState(Qt.Checked)
