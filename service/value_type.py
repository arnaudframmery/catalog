from sqlalchemy import desc, Integer, func, Float

from DB.tables import ValueType, Article
from service.helper import object_as_dict


def get_all_value_types_service(session):
    """recover all possible value types"""
    result = session\
        .query(ValueType.id, ValueType.code)\
        .all()
    return object_as_dict(result)


# Text
def sort_value_type_text_asc(query, subquery):
    """sort in ascending order the values from text value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(func.lower(subquery.c.value))
    return result


def sort_value_type_text_desc(query, subquery):
    """sort in descending order the values from text value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(desc(func.lower(subquery.c.value)))
    return result


# Int
def sort_value_type_int_asc(query, subquery):
    """sort in ascending order the values from int value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(subquery.c.value.cast(Integer))
    return result


def sort_value_type_int_desc(query, subquery):
    """sort in descending order the values from int value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(desc(subquery.c.value.cast(Integer)))
    return result


# Float
def sort_value_type_float_asc(query, subquery):
    """sort in ascending order the values from float value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(subquery.c.value.cast(Float))
    return result


def sort_value_type_float_desc(query, subquery):
    """sort in descending order the values from float value type"""
    result = query\
        .join(subquery, subquery.c.article_id == Article.id)\
        .order_by(desc(subquery.c.value.cast(Float)))
    return result
