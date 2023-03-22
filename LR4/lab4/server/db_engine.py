import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

from lab4.server.config import DATABASE_URL

engine = sql.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)