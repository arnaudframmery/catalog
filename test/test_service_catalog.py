

def test_catalog_create(controller):
	assert controller.get_catalogs() == [], 'failed'

	# Test the creation of 1 catalog
	assert controller.create_catalog('test_1') == 1, 'failed'
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}], 'failed'

	# Test the creation of another catalog
	assert controller.create_catalog('test_2') == 2, 'failed'
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}, {'id': 2, 'name': 'test_2'}], 'failed'


def test_catalog_delete(controller):
	# Test the deletion of 1 catalog
	controller.create_catalog('test_1')
	controller.create_catalog('test_2')
	controller.delete_catalog(1)
	assert controller.get_catalogs() == [{'id': 2, 'name': 'test_2'}], 'failed'

	# Test the deletion of the last catalog
	controller.delete_catalog(2)
	assert controller.get_catalogs() == [], 'failed'


def test_catalog_get_display_setting(controller):
	# Test the recovery of default display setting
	controller.create_catalog('test_1')
	assert controller.get_catalog_display_setting(1) == {'column_number': 5, 'row_number': 4}, 'failed'


def test_catalog_update_display_setting(controller):
	# Test to update catalog display setting
	controller.create_catalog('test_1')
	assert controller.get_catalog_display_setting(1) == {'column_number': 5, 'row_number': 4}, 'failed'
	controller.update_catalog_display_setting(1, row_number=10, column_number=3)
	assert controller.get_catalog_display_setting(1) == {'column_number': 3, 'row_number': 10}, 'failed'
