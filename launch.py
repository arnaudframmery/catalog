from engine import Base, engine, Session
import DB.tables

Base.metadata.create_all(engine)
session = Session()
