from pydantic import BaseModel


class CardDTO(BaseModel):
    id: int
    number: str
    pincode: str
    account_id: int 

    class Config:
        orm_mode=True