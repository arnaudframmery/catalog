from DB.tables import ValueType
from service.helper import object_as_dict


def get_all_value_types_service(session):
    """recover all possible value types"""
    result = session\
        .query(ValueType.id, ValueType.code)\
        .all()
    return object_as_dict(result)
