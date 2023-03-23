from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP

from lab4.server.db import Base


class Transfer(Base):
    __tablename__ = 'transfer'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('card_account.id'))
    operation_type = Column(String, nullable=False)
    operation_name = Column(String)
    completed_at = Column(TIMESTAMP, default=datetime.utcnow)
    amount = Column(Integer)