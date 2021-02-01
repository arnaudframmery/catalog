

def test_catalog_creation(controler):
	assert controler.get_catalogs() == [], 'failed'
	assert controler.create_catalog('test_1') == 1, 'failed'
	assert controler.get_catalogs() == [{'id': 1, 'name': 'test_1'}], 'failed'
	assert controler.create_catalog('test_2') == 2, 'failed'
	assert controler.get_catalogs() == [{'id': 1, 'name': 'test_1'}, {'id': 2, 'name': 'test_2'}], 'failed'


def test_catalog_deletion(controler):
	assert controler.get_catalogs() == [], 'failed'
	controler.create_catalog('test_1')
	assert controler.get_catalogs() == [{'id': 1, 'name': 'test_1'}], 'failed'
	controler.delete_catalog(1)
	assert controler.get_catalogs() == [], 'failed'

	controler.create_catalog('test_1')
	controler.create_catalog('test_2')
	assert controler.get_catalogs() == [{'id': 1, 'name': 'test_1'}, {'id': 2, 'name': 'test_2'}], 'failed'
	controler.delete_catalog(1)
	assert controler.get_catalogs() == [{'id': 2, 'name': 'test_2'}], 'failed'
