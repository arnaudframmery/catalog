

def test_article_create(ctrl_base_1):
    assert ctrl_base_1.get_articles(1, [], None, 'ASC', None) == [], 'failed'
    assert ctrl_base_1.get_articles(2, [], None, 'ASC', None) == [], 'failed'

    # Test the creation of several articles
    assert ctrl_base_1.create_article(1, 'title_1') == 1, 'failed'
    assert ctrl_base_1.create_article(1, 'title_2') == 2, 'failed'
    assert ctrl_base_1.create_article(2, 'title_3') == 3, 'failed'
    assert ctrl_base_1.get_articles(1, [], None, 'ASC', None) == [
        {'title': 'title_1', 'id': 1}, {'title': 'title_2', 'id': 2}
    ], 'failed'
    assert ctrl_base_1.get_articles(2, [], None, 'ASC', None) == [{'title': 'title_3', 'id': 3}], 'failed'


def test_article_update(ctrl_base_1):
    ctrl_base_1.create_article(1, 'title_1')
    ctrl_base_1.create_article(1, 'title_2')
    ctrl_base_1.create_article(2, 'title_3')

    # Test the update of 1 article
    ctrl_base_1.update_article(1, 'title_1_updated')
    assert ctrl_base_1.get_articles(1, [], None, 'ASC', None) == [
        {'title': 'title_1_updated', 'id': 1}, {'title': 'title_2', 'id': 2}
    ], 'failed'


def test_article_delete(ctrl_base_1):
    ctrl_base_1.create_article(1, 'title_1')
    ctrl_base_1.create_article(1, 'title_2')
    ctrl_base_1.create_article(2, 'title_3')

    # Test the deletion of 1 article
    ctrl_base_1.delete_article(2)
    assert ctrl_base_1.get_articles(1, [], None, 'ASC', None) == [{'title': 'title_1', 'id': 1}], 'failed'

    # Test the deletion of the last articles from a catalog
    ctrl_base_1.delete_article(3)
    assert ctrl_base_1.get_articles(2, [], None, 'ASC', None) == [], 'failed'


def test_article_get_detail(ctrl_base_1):
    ctrl_base_1.create_article(1, 'title_1')
    ctrl_base_1.create_article(1, 'title_2')
    ctrl_base_1.create_article(2, 'title_3')

    # Test the recovery of articles detail when there is not any value
    assert ctrl_base_1.get_article_detail(article_id=1, catalog_id=1) == [], 'failed'
    assert ctrl_base_1.get_article_detail(article_id=3, catalog_id=2) == [], 'failed'
