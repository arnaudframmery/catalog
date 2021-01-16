

class Filter:
    def __init__(self, controler, component_id, component_label):
        self.controler = controler
        self.component_id = component_id
        self.component_label = component_label
        self.parent_widget = None

    def get_label(self):
        return self.component_label

    def get_parent_widget(self):
        return self.parent_widget

    def create_widget(self):
        pass

    def apply_filter(self, query):
        pass
