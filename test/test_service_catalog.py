

def test_catalog_creation(controller):
	assert controller.get_catalogs() == [], 'failed'
	assert controller.create_catalog('test_1') == 1, 'failed'
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}], 'failed'
	assert controller.create_catalog('test_2') == 2, 'failed'
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}, {'id': 2, 'name': 'test_2'}], 'failed'


def test_catalog_deletion(controller):
	assert controller.get_catalogs() == [], 'failed'
	controller.create_catalog('test_1')
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}], 'failed'
	controller.delete_catalog(1)
	assert controller.get_catalogs() == [], 'failed'

	controller.create_catalog('test_1')
	controller.create_catalog('test_2')
	assert controller.get_catalogs() == [{'id': 1, 'name': 'test_1'}, {'id': 2, 'name': 'test_2'}], 'failed'
	controller.delete_catalog(1)
	assert controller.get_catalogs() == [{'id': 2, 'name': 'test_2'}], 'failed'
