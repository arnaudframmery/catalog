

component_input_1 = {
    'label': 'component_1',
    'default_value': 'default_value_1',
    'is_sortable': False,
    'filter_code': 'no filter',
}
component_output_1 = {
    'code': 'no filter',
    'default': 'default_value_1',
    'is_sortable': False,
    'label': 'component_1',
}

component_input_2 = {
    'label': 'component_2',
    'default_value': 'default_value_2',
    'is_sortable': True,
    'filter_code': 'category',
}
component_output_2 = {
    'code': 'category',
    'default': 'default_value_2',
    'is_sortable': True,
    'label': 'component_2',
}


def test_component_create(controller_catalog):
    assert controller_catalog.get_components(1) == [], 'failed'
    assert controller_catalog.get_components(2) == [], 'failed'

    controller_catalog.create_components(1, [component_input_1])
    assert controller_catalog.get_components(1) == [
        {**component_output_1, 'id': 1}
    ], 'failed'

    controller_catalog.create_components(2, [component_input_1, component_input_2])
    assert controller_catalog.get_components(2) == [
        {**component_output_1, 'id': 2},
        {**component_output_2, 'id': 3},
    ], 'failed'


def test_component_update(controller_catalog):
    controller_catalog.create_components(1, [component_input_1])
    controller_catalog.update_components([{**component_input_1, 'id': 1, 'label': 'component_1_updated'}])
    assert controller_catalog.get_components(1) == [
        {**component_output_1, 'id': 1, 'label': 'component_1_updated'}
    ], 'failed'

    controller_catalog.create_components(2, [component_input_1, component_input_2])
    controller_catalog.update_components([
        {**component_input_1, 'id': 2, 'label': 'component_1_updated'},
        {**component_input_2, 'id': 3, 'label': 'component_2_updated'},
    ])
    assert controller_catalog.get_components(2) == [
        {**component_output_1, 'id': 2, 'label': 'component_1_updated'},
        {**component_output_2, 'id': 3, 'label': 'component_2_updated'},
    ], 'failed'


def test_component_delete(controller_catalog):
    controller_catalog.create_components(1, [component_input_1])
    controller_catalog.delete_components([1])
    assert controller_catalog.get_components(1) == [], 'failed'

    controller_catalog.create_components(2, [component_input_1, component_input_2])
    controller_catalog.delete_components([1, 2])
    assert controller_catalog.get_components(2) == [], 'failed'

    controller_catalog.create_components(2, [component_input_1, component_input_2])
    controller_catalog.delete_components([2])
    assert controller_catalog.get_components(2) == [{**component_output_1, 'id': 1}], 'failed'


def test_component_get_sortable(controller_catalog):
    controller_catalog.create_components(1, [component_input_1])
    assert controller_catalog.get_sortable_components(1) == [], 'failed'

    controller_catalog.create_components(2, [component_input_1, component_input_2])
    assert controller_catalog.get_sortable_components(2) == [{'label': 'component_2', 'id': 3}], 'failed'
