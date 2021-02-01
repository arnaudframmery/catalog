from DB.tables import Component, Catalog, Filter
from service.helper import object_as_dict


def get_components_service(session, catalog_id):
    """recover all the components about a specific catalog"""
    result = session\
        .query(Component.id, Component.label, Component.is_sortable, Component.default, Filter.code)\
        .join(Filter, Filter.id == Component.filter_id)\
        .join(Catalog)\
        .filter(Catalog.id == catalog_id)\
        .all()
    return object_as_dict(result)


def create_components_service(session, catalog_id, components_data):
    """create a list of new components about a specific catalog"""
    for a_component_data in components_data:
        filter_id = session\
            .query(Filter.id)\
            .filter(Filter.code == a_component_data['filter_code'])\
            .scalar()
        component = Component(
            label=a_component_data['label'],
            default=a_component_data['default_value'],
            is_sortable=a_component_data['is_sortable'],
            filter_id=filter_id,
            catalog_id=catalog_id,
        )
        session.add(component)
    session.commit()


def update_components_service(session, components_data):
    """update a list of components"""
    for a_component_data in components_data:
        filter_id = session\
            .query(Filter.id)\
            .filter(Filter.code == a_component_data['filter_code'])\
            .scalar()
        component = session\
            .query(Component)\
            .filter(Component.id == a_component_data['id'])\
            .one()
        component.label = a_component_data['label']
        component.default = a_component_data['default_value']
        component.is_sortable = a_component_data['is_sortable']
        component.filter_id = filter_id
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
