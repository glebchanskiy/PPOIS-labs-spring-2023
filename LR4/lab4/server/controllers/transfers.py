from fastapi import APIRouter
from fastapi import Response
from fastapi import HTTPException

from lab4.server.db import Session
from lab4.server.repositories import TransferRepository

from lab4.server.dto import TransferDTO


transfer_repository = TransferRepository(Session)
router = APIRouter()


@router.get("/transfers")
def get_transfers() -> list[TransferDTO]:
    return transfer_repository.get_all()


@router.get("/transfers/{id}")
def get_transfer_by_id(id: int) -> TransferDTO:
    return transfer_repository.get_by_id(id)

@router.get("/transfers/by-account-id/{id}")
def get_transfers_by_account_id(id: int) -> list[TransferDTO]:
    return transfer_repository.get_by_account_id(id)


@router.post("/transfers")
def add_transfer(new_transfer: TransferDTO) -> Response:
    transfer_repository.save(new_transfer)
    return Response(status_code=200)


@router.post("/transfers/{id}")
def update_transfer(updated_transfer: TransferDTO, id: int) -> Response:
    raise HTTPException(status_code=500, detail="Tranfers can not be updated!")


@router.delete("/transfers/{id}")
def delete_transfer(id: int) -> Response:
    transfer_repository.delete_by_id(id)
    return Response(status_code=200)