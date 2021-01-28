from DB.tables import Data


def create_data_service(session, data_list):
    """create a list of new data"""
    for data_element in data_list:
        data = Data(
            value=data_element['value'],
            component_id=data_element['component_id'],
            article_id=data_element['article_id'],
        )
        session.add(data)
    session.commit()


def update_data_service(session, data_list):
    """update a list of data"""
    for data_element in data_list:
        data = session\
            .query(Data)\
            .filter(Data.id == data_element['data_id']) \
            .one()
        data.value = data_element['value']
    session.commit()
