from DB.populate import populate_light, populate_init
from UI.main_window import launch_UI
from controller import Controller
from engine import engine, Session
import DB.tables

DB.tables.Base.metadata.create_all(engine)
session = Session()

if session.query(DB.tables.Catalog.id).count() == 0:
    populate_init(session)
    populate_light(session)

controller = Controller(session)
launch_UI(controller)
