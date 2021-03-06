

class Filter:
    """
    Manage which article can be seen in the article area
    """

    def __init__(self, controller, component_id, component_label):
        self.controller = controller
        self.component_id = component_id
        self.component_label = component_label
        self.parent_widget = None

    def __eq__(self, obj):
        return (isinstance(obj, Filter) and
                obj.component_id == self.component_id and
                obj.component_label == self.component_label)

    def get_label(self):
        """recover the label of the filter component label"""
        return self.component_label

    def get_parent_widget(self):
        """recover the widget where the filter display is located"""
        return self.parent_widget

    def create_widget(self):
        """create the filter display"""
        raise NotImplementedError

    def apply_filter(self, catalog_id):
        """filter the articles in function of the widgets current state"""
        raise NotImplementedError

    def reset_filter(self):
        """reset the status of all the widgets to cancel any filtering"""
        raise NotImplementedError
