import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print(f'SQLalchemy version : {sqlalchemy.__version__}')

engine = create_engine(f'sqlite:///{os.path.abspath(os.getcwd())}\\DB\\database.db', echo=True)
Session = sessionmaker(bind=engine)
