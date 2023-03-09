from lab2.app.db.config import DATABASE_URI

import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


class DbConnect:
    def __init__(self) -> None:
        self.engine = sql.create_engine(DATABASE_URI)
        try:
            self.engine.connect()
        except SQLAlchemyError as err:
            print('Connection refused.\nCheck connection')
            raise SQLAlchemyError

    def get_sessionmaker(self):
        return sessionmaker(bind=self.engine)