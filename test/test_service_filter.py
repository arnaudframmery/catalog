from filter.filter_category import FilterCategory


def test_filter_get_all(ctrl_base_3):
    # Test the recovery of all the possible filters
    assert ctrl_base_3.get_all_filters() == [
        {'code': 'no filter', 'id': 1},
        {'code': 'category', 'id': 2},
    ], 'failed'


def test_filter_get(ctrl_base_3):
    # Test the recovery of all the filters from a specific catalog
    assert ctrl_base_3.get_filters(1) == [], 'failed'
    assert ctrl_base_3.get_filters(2) == [FilterCategory(ctrl_base_3, 3, 'component_2')], 'failed'


def test_filter_get_categories(ctrl_base_3):
    # Test the recovery of all the categories for a component with a category filter
    assert ctrl_base_3.get_categories(3) == ['value_3', 'default_value_2'], 'failed'


def test_filter_apply_categories(ctrl_base_3):
    # Test the application of a category filter
    categories = ctrl_base_3.get_categories(3)
    parameters = {'catalog_id': 2, 'component_id': 3, 'subquery': False}
    assert ctrl_base_3.apply_categories(**parameters, categories=categories) == [
        {'article_id': 2, 'component_id': 3},
        {'article_id': 3, 'component_id': 3},
        {'article_id': 4, 'component_id': 3},
    ], 'failed'
    assert ctrl_base_3.apply_categories(**parameters, categories=['value_3']) == [
        {'article_id': 2, 'component_id': 3},
    ], 'failed'
    assert ctrl_base_3.apply_categories(**parameters, categories=['default_value_2']) == [
        {'article_id': 3, 'component_id': 3},
        {'article_id': 4, 'component_id': 3},
    ], 'failed'
