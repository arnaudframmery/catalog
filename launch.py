from DB.populate import populate_light
from UI.main_window import launch_UI
from controller import controller
from engine import engine, Session
import DB.tables

DB.tables.Base.metadata.create_all(engine)
session = Session()

if session.query(DB.tables.Catalog.id).count() == 0:
    populate_light(session)

controller = controller(session)
launch_UI(controller)
