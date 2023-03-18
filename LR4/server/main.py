from fastapi import FastAPI
from fastapi import Response, HTTPException

from typing import Optional

from logging.config import dictConfig
from log_config import log_config
import logging

import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

from models import Card, CardAccount, Transfer
from dto import CardDTO, CardAccountDTO, TransferDTO


engine = sql.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


dictConfig(log_config)
logger = logging.getLogger("app")


app = FastAPI(
    title="Bank Server",
    debug=True,
)


@app.get("/cards")
def get_cards() -> list[CardDTO]:

    with Session() as session:
        cards = session.query(Card).all()

    return [CardDTO.from_orm(c) for c in cards]


@app.get("/cards/{id}")
def get_card_by_id(id: int) -> Optional[CardDTO]:

    with Session() as session:
        target_card = session.query(Card).filter(Card.id == id).first()

    return CardDTO.from_orm(target_card) if target_card is not None else None

@app.get("/cards/by-number/{number}")
def get_card_by_number(number: str) -> Optional[CardDTO]:

    with Session() as session:
        target_card = session.query(Card).filter(Card.number==number).first()
        # logger.info("target_card", target_card)

    return CardDTO.from_orm(target_card) if target_card is not None else None

@app.post("/cards")
def add_card(new_card: CardDTO) -> Response:
    
    with Session() as session:
        session.add(Card(**new_card.dict()))
        session.commit()

    return Response(status_code=200)

@app.post("/cards/{id}")
def update_card(updated_card: CardDTO, id: int) -> Response:

    with Session() as session:
        target_card = session.query(Card).filter(Card.id == id).first()
        target_card.number = updated_card.number
        target_card.pincode = updated_card.pincode
        target_card.account_id = updated_card.account_id
        session.commit()
    
    return Response(status_code=200)

@app.delete("/cards/{id}")
def delete_card(id: int) -> Response:

    with Session() as session:
        card_to_be_deleted = session.query(Card).filter(Card.id == id).first()
        session.delete(card_to_be_deleted)
        session.commit()

    return Response(status_code=200)


@app.get("/accounts")
def get_accounts() -> list[CardAccountDTO]:

    with Session() as session:
        accounts = session.query(CardAccount).all()

    return [CardAccountDTO.from_orm(a) for a in accounts]


@app.get("/accounts/{id}")
def get_account_by_id(id: int) -> Optional[CardAccountDTO]:

    with Session() as session:
        target_account = session.query(CardAccount).filter(
            CardAccount.id == id).first()

    return CardAccountDTO.from_orm(target_account) if target_account is not None else None

@app.post("/accounts")
def add_accounts(new_account: CardAccountDTO) -> Response:
    
    with Session() as session:
        session.add(CardAccount(**new_account.dict()))
        session.commit()

    return Response(status_code=200)

@app.post("/accounts/{id}")
def update_account(updated_account: CardAccountDTO, id: int) -> Response:

    with Session() as session:
        target_account = session.query(CardAccount).filter(CardAccount.id == id).first()
        target_account.number = updated_account.number
        target_account.currency = updated_account.currency
        target_account.balance = updated_account.balance
        session.commit()
        logger.info(target_account.balance)
        logger.info(updated_account.balance)
    
    return Response(status_code=200)

@app.delete("/accounts/{id}")
def delete_account(id: int) -> Response:

    with Session() as session:
        account_to_be_deleted = session.query(CardAccount).filter(CardAccount.id == id)
        session.delete(account_to_be_deleted)
        session.commit()

    return Response(status_code=200)


@app.get("/transfers")
def get_transfers() -> list[TransferDTO]:

    with Session() as session:
        transfers = session.query(Transfer).all()

    return [TransferDTO.from_orm(t) for t in transfers]


@app.get("/transfers/{id}")
def get_transfer_by_id(id: int) -> Optional[TransferDTO]:

    with Session() as session:
        target_transfer = session.query(Transfer).filter(
            Transfer.id == id).first()

    return TransferDTO.from_orm(target_transfer) if target_transfer is not None else None

@app.get("/transfers/by-account-id/{id}")
def get_transfers_by_account_id(id: int) -> list[TransferDTO]:

    with Session() as session:
        transfers = session.query(Transfer).filter(
            Transfer.account_id == id).all()

    return [TransferDTO.from_orm(t) for t in transfers]


@app.post("/transfers")
def add_transfer(new_transfer: TransferDTO) -> Response:
    
    with Session() as session:
        session.add(Transfer(**new_transfer.dict()))
        session.commit()

    return Response(status_code=200)


@app.post("/transfers/{id}")
def update_transfer(updated_transfer: TransferDTO, id: int) -> Response:
    raise HTTPException(status_code=500, detail="Tranfers can not be updated!")


@app.delete("/transfers/{id}")
def delete_transfer(id: int) -> Response:

    with Session() as session:
        transfer_to_be_deleted = session.query(Transfer).filter(Transfer.id == id)
        session.delete(transfer_to_be_deleted)
        session.commit()

    return Response(status_code=200)