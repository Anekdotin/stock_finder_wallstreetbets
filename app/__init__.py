from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI_0


# session one is info
# engine 1
engine = create_engine(SQLALCHEMY_DATABASE_URI_0)
Base = declarative_base()
Base.metadata.reflect(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()









Base.metadata.create_all(engine)

