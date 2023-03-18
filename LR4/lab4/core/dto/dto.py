from pydantic import BaseModel, Field
from datetime import datetime


class CardDTO(BaseModel):
    id: int
    number: str # = Field(constr(max_length=16))
    pincode: str # = Field(constr(max_length=4))
    account_id: int 

    class Config:
        orm_mode=True

class CardAccountDTO(BaseModel):
    id: int
    number: str
    currency: str
    balance: int

    class Config:
        orm_mode=True

class TransferDTO(BaseModel):
    id: int = None
    account_id: int
    operation_type: str
    operation_name: str
    completed_at: datetime = None
    amount: int = None

    class Config:
        orm_mode=True