from PyQt5 import QtWidgets
from UI.qt_ui.catalog_frame_UI import Ui_Form


class CatalogFrameWidget(QtWidgets.QWidget, Ui_Form):

    def __init__(self, sortable_components, *args, obj=None, **kwargs):
        super(CatalogFrameWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.sortable_components = sortable_components
        self.sort_combo_box.insertItems(
            0,
            ['No sorting'] + [a_component['label'] for a_component in self.sortable_components]
        )
        self.horizontalLayout.insertStretch(0)

    def get_sorting_component_id(self, component_index):
        if component_index == 0:
            return None
        else:
            return self.sortable_components[component_index - 1]['id']
