

def test_value_type_get_all(controller):
    # Test the recovery of all the possible value types
    assert controller.get_all_value_types() == [
        {'code': 'text', 'id': 1},
        {'code': 'int', 'id': 2},
    ], 'failed'
