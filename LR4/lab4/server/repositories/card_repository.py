from sqlalchemy.orm import sessionmaker
from lab4.server.repositories.abstract_repository import AbstractRepository

from lab4.server.models import Card
from lab4.server.dto import CardDTO


class CardRepository(AbstractRepository):

    def __init__(self, session: sessionmaker) -> None:
        super().__init__()
        self.__Session = session


    def get_by_id(self, id: int) -> CardDTO:
        with self.__Session() as session:
            card = session.query(Card).filter(Card.id == id).first()

        return CardDTO.from_orm(card) if card is not None else None

    def get_all(self) -> list[CardDTO]:
        with self.__Session() as session:
            cards = session.query(Card).all()

        return [CardDTO.from_orm(c) for c in cards]

    def save(self, new_card: CardDTO):
        with self.__Session() as session: 
            session.add(Card(**new_card.dict()))
            session.commit()
            

    def update(self, updated_card: CardDTO):
        with self.__Session() as session:
            card_to_be_updated = session.query(Card).filter(
                updated_card.id == id).first()
            card_to_be_updated.number = updated_card.number
            card_to_be_updated.pincode = updated_card.pincode
            card_to_be_updated.account_id = updated_card.account_id
            session.commit()

    def delete_by_id(self, id: int):
        with self.__Session() as session:
            card_to_be_deleted = session.query(
                Card).filter(Card.id == id).first()
            session.delete(card_to_be_deleted)
            session.commit()

    def get_by_number(self, number: str):
        with self.__Session() as session:
            card = session.query(Card).filter(
                Card.number == number).first()

        return CardDTO.from_orm(card) if card is not None else None
