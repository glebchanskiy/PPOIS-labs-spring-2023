from sqlalchemy.orm import Session
from lab4.server.repositories.abstract_repository import AbstractRepository

from lab4.server.models import CardAccount
from lab4.server.dto import CardAccountDTO


class CardAccountRepository(AbstractRepository):

    def __init__(self, Session: Session) -> None:
        super().__init__()
        self.__Session = Session


    def get_by_id(self, id: int) -> CardAccountDTO:
        with self.__Session() as session:
            target_account = session.query(CardAccount).filter(CardAccount.id == id).first()

        return CardAccountDTO.from_orm(target_account) if target_account is not None else None

    def get_all(self) -> list[CardAccountDTO]:
        with self.__Session() as session:
            accounts = session.query(CardAccount).all()

        return [CardAccountDTO.from_orm(a) for a in accounts]

    def save(self, new_account: CardAccountDTO):
        with self.__Session() as session: 
            session.add(CardAccount(**new_account.dict()))
            session.commit()
            

    def update(self, updated_account: CardAccountDTO):
        with self.__Session() as session:
            target_account = session.query(CardAccount).filter(
                updated_account.id == id).first()
            target_account.number = updated_account.number
            target_account.pincode = updated_account.pincode
            target_account.account_id = updated_account.account_id
            session.commit()

    def delete_by_id(self, id: int):
        with self.__Session() as session:
            account_to_be_deleted = session.query(
                CardAccount).filter(CardAccount.id == id).first()
            session.delete(account_to_be_deleted)
            session.commit()