from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class CardAccount(Base):
    __tablename__ = 'card_account'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    balance = Column(Integer)