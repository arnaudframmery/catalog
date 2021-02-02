

def test_article_create(controller_catalog):
    assert controller_catalog.get_articles(1, [], None, 'ASC') == [], 'failed'
    assert controller_catalog.get_articles(2, [], None, 'ASC') == [], 'failed'

    assert controller_catalog.create_article(1, 'title_1') == 1, 'failed'
    assert controller_catalog.create_article(1, 'title_2') == 2, 'failed'
    assert controller_catalog.create_article(2, 'title_3') == 3, 'failed'
    assert controller_catalog.get_articles(1, [], None, 'ASC') == [
        {'title': 'title_1', 'id': 1}, {'title': 'title_2', 'id': 2}
    ], 'failed'
    assert controller_catalog.get_articles(2, [], None, 'ASC') == [{'title': 'title_3', 'id': 3}], 'failed'


def test_article_update(controller_catalog):
    controller_catalog.create_article(1, 'title_1')
    controller_catalog.create_article(1, 'title_2')
    controller_catalog.create_article(2, 'title_3')

    controller_catalog.update_article(1, 'title_1_updated')
    assert controller_catalog.get_articles(1, [], None, 'ASC') == [
        {'title': 'title_1_updated', 'id': 1}, {'title': 'title_2', 'id': 2}
    ], 'failed'

    controller_catalog.update_article(3, 'title_3_updated')
    assert controller_catalog.get_articles(2, [], None, 'ASC') == [{'title': 'title_3_updated', 'id': 3}], 'failed'


def test_article_delete(controller_catalog):
    controller_catalog.create_article(1, 'title_1')
    controller_catalog.create_article(1, 'title_2')
    controller_catalog.create_article(2, 'title_3')

    controller_catalog.delete_article(2)
    assert controller_catalog.get_articles(1, [], None, 'ASC') == [{'title': 'title_1', 'id': 1}], 'failed'

    controller_catalog.delete_article(3)
    assert controller_catalog.get_articles(2, [], None, 'ASC') == [], 'failed'


def test_article_get_detail(controller_catalog):
    controller_catalog.create_article(1, 'title_1')
    controller_catalog.create_article(1, 'title_2')
    controller_catalog.create_article(2, 'title_3')

    assert controller_catalog.get_article_detail(1, 1) == [], 'failed'
    assert controller_catalog.get_article_detail(3, 2) == [], 'failed'
