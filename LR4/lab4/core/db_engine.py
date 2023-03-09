import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from lab4.core.config import DATABASE_URI

class DbEngine:
   def __init__(self) -> None:
       self._engine = sql.create_engine(DATABASE_URI)
       self._sessionmaker = sessionmaker(bind=self._engine)
   
   def get_session(self) -> None:
      return self._sessionmaker()
