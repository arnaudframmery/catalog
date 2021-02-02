

def test_value_create(ctrl_base_2):
    # Test the creation of 1 value (must have default value for the other components)
    ctrl_base_2.create_values([{'component_id': 1, 'value': 'value_1', 'article_id': 1}])
    assert ctrl_base_2.get_article_detail(article_id=1, catalog_id=1) == [
        {'component_id': 1, 'label': 'component_1', 'value': 'value_1', 'value_id': 1}
    ], 'failed'
    assert ctrl_base_2.get_article_detail(article_id=2, catalog_id=2) == [
        {'component_id': 2, 'label': 'component_1', 'value': 'default_value_1', 'value_id': None},
        {'component_id': 3, 'label': 'component_2', 'value': 'default_value_2', 'value_id': None},
    ], 'failed'

    # Test the creation of several values
    ctrl_base_2.create_values([
        {'component_id': 2, 'value': 'value_2', 'article_id': 2},
        {'component_id': 3, 'value': 'value_3', 'article_id': 2},
    ])
    assert ctrl_base_2.get_article_detail(article_id=1, catalog_id=1) == [
        {'component_id': 1, 'label': 'component_1', 'value': 'value_1', 'value_id': 1}
    ], 'failed'
    assert ctrl_base_2.get_article_detail(article_id=2, catalog_id=2) == [
        {'component_id': 2, 'label': 'component_1', 'value': 'value_2', 'value_id': 2},
        {'component_id': 3, 'label': 'component_2', 'value': 'value_3', 'value_id': 3},
    ], 'failed'


def test_value_update(ctrl_base_2):
    ctrl_base_2.create_values([
        {'component_id': 1, 'value': 'value_1', 'article_id': 1},
        {'component_id': 2, 'value': 'value_2', 'article_id': 2},
        {'component_id': 3, 'value': 'value_3', 'article_id': 2},
    ])

    # Test the update of 1 value
    ctrl_base_2.update_values([{'value': 'value_1_updated', 'value_id': 1}, ])
    assert ctrl_base_2.get_article_detail(article_id=1, catalog_id=1) == [
        {'component_id': 1, 'label': 'component_1', 'value': 'value_1_updated', 'value_id': 1}
    ], 'failed'
    assert ctrl_base_2.get_article_detail(article_id=2, catalog_id=2) == [
        {'component_id': 2, 'label': 'component_1', 'value': 'value_2', 'value_id': 2},
        {'component_id': 3, 'label': 'component_2', 'value': 'value_3', 'value_id': 3},
    ], 'failed'

    # Test the update of several values
    ctrl_base_2.update_values([
        {'value': 'value_2_updated', 'value_id': 2},
        {'value': 'value_3_updated', 'value_id': 3},
    ])
    assert ctrl_base_2.get_article_detail(article_id=1, catalog_id=1) == [
        {'component_id': 1, 'label': 'component_1', 'value': 'value_1_updated', 'value_id': 1}
    ], 'failed'
    assert ctrl_base_2.get_article_detail(article_id=2, catalog_id=2) == [
        {'component_id': 2, 'label': 'component_1', 'value': 'value_2_updated', 'value_id': 2},
        {'component_id': 3, 'label': 'component_2', 'value': 'value_3_updated', 'value_id': 3},
    ], 'failed'
