from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    account_id = Column(Integer, ForeignKey('card_account.id'))