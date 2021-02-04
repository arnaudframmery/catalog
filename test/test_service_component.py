

component_input_1 = {
    'label': 'component_1',
    'default_value': 'default_value_1',
    'is_sortable': False,
    'filter_code': 'no filter',
    'type_code': 'text',
    'previous_type_code': 'text',
}
component_output_1 = {
    'filter_code': 'no filter',
    'type_code': 'text',
    'default': 'default_value_1',
    'is_sortable': False,
    'label': 'component_1',
}

component_input_2 = {
    'label': 'component_2',
    'default_value': 'default_value_2',
    'is_sortable': True,
    'filter_code': 'category',
    'type_code': 'text',
    'previous_type_code': 'text',
}
component_output_2 = {
    'filter_code': 'category',
    'type_code': 'text',
    'default': 'default_value_2',
    'is_sortable': True,
    'label': 'component_2',
}


def test_component_create(ctrl_base_1):
    assert ctrl_base_1.get_components(1) == [], 'failed'
    assert ctrl_base_1.get_components(2) == [], 'failed'

    # Test the creation of 1 component
    ctrl_base_1.create_components(1, [component_input_1])
    assert ctrl_base_1.get_components(1) == [
        {**component_output_1, 'id': 1}
    ], 'failed'

    # Test the creation of several components
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    assert ctrl_base_1.get_components(2) == [
        {**component_output_1, 'id': 2},
        {**component_output_2, 'id': 3},
    ], 'failed'


def test_component_update(ctrl_base_1):
    # Test the update of 1 component
    ctrl_base_1.create_components(1, [component_input_1])
    ctrl_base_1.update_components([{**component_input_1, 'id': 1, 'label': 'component_1_updated'}])
    assert ctrl_base_1.get_components(1) == [
        {**component_output_1, 'id': 1, 'label': 'component_1_updated'}
    ], 'failed'

    # Test the update of several components
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    ctrl_base_1.update_components([
        {**component_input_1, 'id': 2, 'label': 'component_1_updated'},
        {**component_input_2, 'id': 3, 'label': 'component_2_updated'},
    ])
    assert ctrl_base_1.get_components(2) == [
        {**component_output_1, 'id': 2, 'label': 'component_1_updated'},
        {**component_output_2, 'id': 3, 'label': 'component_2_updated'},
    ], 'failed'

    # Test the update with a change in value type
    ctrl_base_1.create_article(2, 'title_1')
    ctrl_base_1.create_article(2, 'title_2')
    ctrl_base_1.create_values([{'component_id': 3, 'value': '0100', 'article_id': 1}])
    ctrl_base_1.create_values([{'component_id': 3, 'value': 'cent', 'article_id': 1}])
    ctrl_base_1.update_components([
        {**component_input_2, 'id': 3, 'label': 'component_2_updated', 'default_value': '007', 'type_code': 'int'},
    ])
    assert ctrl_base_1.get_components(2) == [
        {**component_output_1, 'id': 2, 'label': 'component_1_updated'},
        {**component_output_2, 'id': 3, 'label': 'component_2_updated', 'default': '7', 'type_code': 'int'},
    ], 'failed'
    assert ctrl_base_1.get_values(component_id=3) == [{'value': '100', 'id': 1}], 'failed'


def test_component_delete(ctrl_base_1):
    # Test the deletion of 1 component
    ctrl_base_1.create_components(1, [component_input_1])
    ctrl_base_1.delete_components([1])
    assert ctrl_base_1.get_components(1) == [], 'failed'

    # Test the deletion of several components
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    ctrl_base_1.delete_components([1, 2])
    assert ctrl_base_1.get_components(2) == [], 'failed'

    # Test the deletion of 1 component out of 2
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    ctrl_base_1.delete_components([2])
    assert ctrl_base_1.get_components(2) == [{**component_output_1, 'id': 1}], 'failed'


def test_component_get_sortable(ctrl_base_1):
    # Test the recovery of 0 sortable component
    ctrl_base_1.create_components(1, [component_input_1])
    assert ctrl_base_1.get_sortable_components(1) == [], 'failed'

    # Test the recovery of 1 sortable component
    ctrl_base_1.create_components(2, [component_input_1, component_input_2])
    assert ctrl_base_1.get_sortable_components(2) == [{'label': 'component_2', 'id': 3}], 'failed'

    # Test the recovery of several sortable components
    ctrl_base_1.create_components(2, [{**component_input_2, 'label': 'component_3'}])
    assert ctrl_base_1.get_sortable_components(2) == [
        {'label': 'component_2', 'id': 3},
        {'label': 'component_3', 'id': 4},
    ], 'failed'
