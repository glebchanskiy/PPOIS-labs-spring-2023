from pydantic import BaseModel


class CardAccountDTO(BaseModel):
    id: int
    number: str
    currency: str
    balance: int

    class Config:
        orm_mode=True