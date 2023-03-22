from sqlalchemy.orm import sessionmaker
from lab4.server.repositories.abstract_repository import AbstractRepository

from lab4.server.models import CardAccount
from lab4.server.dto import CardAccountDTO


class CardAccountRepository(AbstractRepository):

    def __init__(self, session: sessionmaker) -> None:
        super().__init__()
        self.__Session = session

    def get_by_id(self, id: int) -> CardAccountDTO:
        with self.__Session() as session:
            target_account = session.query(CardAccount).filter(
                CardAccount.id == id).first()

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
            account_to_be_updated = session.query(CardAccount).filter(
                CardAccount.id == updated_account.id).first()
            account_to_be_updated.balance = updated_account.balance
            account_to_be_updated.currency = updated_account.currency
            account_to_be_updated.number = updated_account.number
            session.commit()

    def delete_by_id(self, id: int):
        with self.__Session() as session:
            account_to_be_deleted = session.query(
                CardAccount).filter(CardAccount.id == id).first()
            session.delete(account_to_be_deleted)
            session.commit()
