import uvicorn

from fastapi import FastAPI
from fastapi import Response, HTTPException

from typing import Optional

import logging
from logging.config import dictConfig
from lab4.server.log_config import log_config

import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

from lab4.server.config import DATABASE_URL
from lab4.server.dto import CardDTO, CardAccountDTO, TransferDTO

from lab4.server.repositories.card_repository import CardRepository
from lab4.server.repositories.card_account_repository import CardAccountRepository
from lab4.server.repositories.transfer_repository import TransferRepository


dictConfig(log_config)
logger = logging.getLogger("app")

engine = sql.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

card_repository = CardRepository(Session)
card_account_repository = CardAccountRepository(Session)
transfer_repository = TransferRepository(Session)




app = FastAPI(
    title="Bank Server",
    debug=True,
)


@app.get("/cards")
def get_cards() -> list[CardDTO]:
    return card_repository.get_all()


@app.get("/cards/{id}")
def get_card_by_id(id: int) -> Optional[CardDTO]:
    return card_repository.get_by_id(id)

@app.get("/cards/by-number/{number}")
def get_card_by_number(number: str) -> Optional[CardDTO]:
    return card_repository.get_by_number(number)

@app.post("/cards")
def add_card(new_card: CardDTO) -> Response:
    card_repository.save(new_card)
    return Response(status_code=200)

@app.post("/cards/{id}")
def update_card(updated_card: CardDTO, id: int) -> Response:
    updated_card.id = id
    card_repository.update(updated_card)
    return Response(status_code=200)

@app.delete("/cards/{id}")
def delete_card(id: int) -> Response:
    card_repository.delete_by_id(id)
    return Response(status_code=200)


@app.get("/accounts")
def get_accounts() -> list[CardAccountDTO]:
    return card_account_repository.get_all()



@app.get("/accounts/{id}")
def get_account_by_id(id: int) -> Optional[CardAccountDTO]:
    return card_account_repository.get_by_id(id)

@app.post("/accounts")
def add_accounts(new_account: CardAccountDTO) -> Response:
    card_account_repository.save(new_account)
    return Response(status_code=200)

@app.post("/accounts/{id}")
def update_account(updated_account: CardAccountDTO, id: int) -> Response:
    updated_account.id = id
    card_account_repository.update(update_account)
    return Response(status_code=200)

@app.delete("/accounts/{id}")
def delete_account(id: int) -> Response:
    card_account_repository.delete_by_id(id)
    return Response(status_code=200)


@app.get("/transfers")
def get_transfers() -> list[TransferDTO]:
    return transfer_repository.get_all()


@app.get("/transfers/{id}")
def get_transfer_by_id(id: int) -> Optional[TransferDTO]:
    return transfer_repository.get_by_id(id)

@app.get("/transfers/by-account-id/{id}")
def get_transfers_by_account_id(id: int) -> list[TransferDTO]:
    return transfer_repository.get_by_account_id(id)


@app.post("/transfers")
def add_transfer(new_transfer: TransferDTO) -> Response:
    transfer_repository.save(new_transfer)
    return Response(status_code=200)


@app.post("/transfers/{id}")
def update_transfer(updated_transfer: TransferDTO, id: int) -> Response:
    raise HTTPException(status_code=500, detail="Tranfers can not be updated!")


@app.delete("/transfers/{id}")
def delete_transfer(id: int) -> Response:
    transfer_repository.delete_by_id(id)
    return Response(status_code=200)