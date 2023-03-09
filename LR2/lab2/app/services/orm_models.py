from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    fullname = Column(String)
    account_number = Column(String, primary_key=True)
    address = Column(String)
    mobile = Column(String)
    landline = Column(String)
