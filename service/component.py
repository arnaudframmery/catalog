from DB.tables import Component, Catalog, Filter, ValueType
from mapping import VALUE_TYPE_MAPPING
from service.helper import object_as_dict
from service.value import get_values_service, update_values_service, delete_value_service


def get_components_service(session, catalog_id):
    """recover all the components about a specific catalog"""
    result = session\
        .query(Component.id,
               Component.label,
               Component.is_sortable,
               Component.default,
               Filter.code.label('filter_code'),
               ValueType.code.label('type_code'))\
        .join(Filter, Filter.id == Component.filter_id)\
        .join(ValueType, ValueType.id == Component.value_type_id)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .all()
    return object_as_dict(result)


def get_sortable_components_service(session, catalog_id):
    """recover all components that can be sorted about a specific catalog"""
    result = session\
        .query(Component.label, Component.id, ValueType.code)\
        .join(Catalog)\
        .join(ValueType)\
        .filter(Catalog.id == catalog_id)\
        .filter(Component.is_sortable)\
        .all()
    return object_as_dict(result)


def create_components_service(session, catalog_id, components_data):
    """create a list of new components about a specific catalog"""
    for a_component_data in components_data:
        filter_id = session\
            .query(Filter.id)\
            .filter(Filter.code == a_component_data['filter_code'])\
            .scalar()
        value_type_id = session\
            .query(ValueType.id)\
            .filter(ValueType.code == a_component_data['type_code'])\
            .scalar()
        default_value = VALUE_TYPE_MAPPING[a_component_data['type_code']].recovery_process(
            a_component_data['default_value']
        )
        component = Component(
            label=a_component_data['label'],
            default=default_value,
            is_sortable=a_component_data['is_sortable'],
            filter_id=filter_id,
            catalog_id=catalog_id,
            value_type_id=value_type_id,
        )
        session.add(component)
    session.commit()


def update_component_value_type_service(session, component_id, value_type_code, previous_value_type_code):
    """update the values about a specific component to match a value type"""
    values = get_values_service(session, component_id)
    for a_value in values:
        new_value = (
            VALUE_TYPE_MAPPING[value_type_code].recovery_process(a_value['value'])
            if VALUE_TYPE_MAPPING[value_type_code].is_recovery_accepted(previous_value_type_code)
            else None
        )
        if new_value:
            update_values_service(session, [{'value_id': a_value['id'], 'value': new_value, 'code': value_type_code}])
        else:
            delete_value_service(session, a_value['id'])


def update_components_service(session, components_data):
    """update a list of components"""
    for a_component_data in components_data:
        filter_id = session\
            .query(Filter.id)\
            .filter(Filter.code == a_component_data['filter_code'])\
            .scalar()
        value_type_id = session\
            .query(ValueType.id)\
            .filter(ValueType.code == a_component_data['type_code'])\
            .scalar()
        component = session\
            .query(Component)\
            .filter(Component.id == a_component_data['id'])\
            .one()
        default_value = VALUE_TYPE_MAPPING[a_component_data['type_code']].recovery_process(
            a_component_data['default_value']
        )
        component.label = a_component_data['label']
        component.default = default_value
        component.is_sortable = a_component_data['is_sortable']
        component.filter_id = filter_id
        component.value_type_id = value_type_id
        if a_component_data['type_code'] != a_component_data['previous_type_code']:
            update_component_value_type_service(
                session,
                a_component_data['id'],
                a_component_data['type_code'],
                a_component_data['previous_type_code'],
            )
    session.commit()


def delete_components_service(session, components_id):
    """delete a list of components"""
    for a_component_id in components_id:
        component = session\
            .query(Component)\
            .filter(Component.id == a_component_id)\
            .one()
        session.delete(component)
    session.commit()
