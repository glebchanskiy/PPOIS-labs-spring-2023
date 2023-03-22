from sqlalchemy.orm import Session
from lab4.server.repositories.abstract_repository import AbstractRepository

from lab4.server.models import Transfer
from lab4.server.dto import TransferDTO


class TransferRepository(AbstractRepository):

    def __init__(self, Session: Session) -> None:
        super().__init__()
        self.__Session = Session


    def get_by_id(self, id: int) -> TransferDTO:
        with self.__Session() as session:
            transfer = session.query(Transfer).filter(Transfer.id == id).first()

        return TransferDTO.from_orm(transfer) if transfer is not None else None
    
    def get_by_account_id(self, id: int) -> list[TransferDTO]:
        with Session() as session:
            transfers = session.query(Transfer).filter(
                Transfer.account_id == id).all()
            
        return [TransferDTO.from_orm(t) for t in transfers]

    def get_all(self) -> list[TransferDTO]:
        with self.__Session() as session:
            transfers = session.query(Transfer).all()

        return [TransferDTO.from_orm(t) for t in transfers]

    def save(self, new_transfer: TransferDTO):
        with self.__Session() as session: 
            session.add(Transfer(**new_transfer.dict()))
            session.commit()
            

    def update(self, updated_transfer: TransferDTO):
        with self.__Session() as session:
            transfer_to_be_updated = session.query(Transfer).filter(
                updated_transfer.id == id).first()
            transfer_to_be_updated.number = updated_transfer.number
            transfer_to_be_updated.pincode = updated_transfer.pincode
            transfer_to_be_updated.account_id = updated_transfer.account_id
            session.commit()

    def delete_by_id(self, id: int):
        with self.__Session() as session:
            transfer_to_be_deleted = session.query(
                Transfer).filter(Transfer.id == id).first()
            session.delete(transfer_to_be_deleted)
            session.commit()