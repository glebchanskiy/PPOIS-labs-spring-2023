from sqlalchemy import Column, Integer, String

from lab4.server.db import Base

class CardAccount(Base):
    __tablename__ = 'card_account'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    balance = Column(Integer)