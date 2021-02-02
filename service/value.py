from DB.tables import Value


def create_values_service(session, value_list):
    """create a list of new value"""
    for value_element in value_list:
        new_value = Value(
            value=value_element['value'],
            component_id=value_element['component_id'],
            article_id=value_element['article_id'],
        )
        session.add(new_value)
    session.commit()


def update_values_service(session, value_list):
    """update a list of value"""
    for a_value in value_list:
        value_to_update = session\
            .query(Value)\
            .filter(Value.id == a_value['value_id']) \
            .one()
        value_to_update.value = a_value['value']
    session.commit()
