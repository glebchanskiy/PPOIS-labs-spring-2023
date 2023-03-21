import requests

from lab4.core.repositories.abstract_repository import AbstractRepository
from lab4.core.dto.dto import TransferDTO
from lab4.core.config import SERVER_IP, SERVER_PORT

class TransferRepository(AbstractRepository):
    __api_url: str = f"{SERVER_IP}:{SERVER_PORT}"
    
    def get_by_id(self, id: int) -> TransferDTO:
        response = requests.get(f"http://{self.__api_url}/transfers/{id}")
        if response.status_code == 200:
            json_card = response.json()
            return TransferDTO.parse_obj(json_card)
        else:
            return None

    def get_all_by_account_id(self, id: int) -> list[TransferDTO]:
        response = requests.get(f"http://{self.__api_url}/transfers/by-account-id/{id}")
        if response.status_code == 200:
            json_transfers = response.json()
            return [TransferDTO.parse_obj(t) for t in json_transfers]
        else:
            return []
    
    def get_all(self) -> list[TransferDTO]:
        response = requests.get(f"http://{self.__api_url}/transfers")
        if response.status_code == 200:
            json_transfers = response.json()
            cards = [TransferDTO.parse_obj(t) for t in json_transfers]
            return cards
        else:
            return []
        
    def save(self, transfer: TransferDTO) -> None:
        requests.post(url=f"http://{self.__api_url}/transfers", data=transfer.json())

    def delete(self):
        pass

    def update(self):
        pass
    
        