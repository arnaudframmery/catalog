from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from filter.filter import Filter


class FilterCategory(Filter):
    def __init__(self, controler, component_id, component_label):
        super().__init__(controler, component_id, component_label)
        self.categories = self.controler.get_categories(self.component_id)
        self.widgets = []

    def create_widget(self):
        self.parent_widget = QtWidgets.QGroupBox(self.component_label)
        layout = QVBoxLayout()
        for a_category in self.categories:
            check_box = QtWidgets.QCheckBox(a_category)
            check_box.setCheckState(Qt.Checked)
            self.widgets.append(check_box)
            layout.addWidget(check_box)
        self.parent_widget.setLayout(layout)

    def apply_filter(self, catalog_id):
        query_categories = []
        for i in range(len(self.widgets)):
            if self.widgets[i].isChecked():
                query_categories.append(self.categories[i])
        return self.controler.apply_categories(catalog_id, self.component_id, query_categories)
