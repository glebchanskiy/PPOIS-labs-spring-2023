import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from lab4.server.config import DATABASE_URL

engine = sql.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


Base = declarative_base()