from sqlalchemy import Column, Integer, String, ForeignKey

from lab4.server.db import Base


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    account_id = Column(Integer, ForeignKey('CardAccount.id'))