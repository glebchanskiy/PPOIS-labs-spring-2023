from pydantic import BaseModel
from datetime import datetime


class TransferDTO(BaseModel):
    id: int = None
    account_id: int
    operation_type: str
    operation_name: str
    completed_at: datetime = None
    amount: int = None

    class Config:
        orm_mode=True