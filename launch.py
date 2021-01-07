from DB.populate import populate_light
from UI.main_window import launch_UI
from controler import Controler
from engine import Base, engine, Session
import DB.tables

Base.metadata.create_all(engine)
session = Session()

populate_light(session)
controler = Controler(session)
launch_UI(controler)
