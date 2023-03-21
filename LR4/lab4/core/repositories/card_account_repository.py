import requests

from lab4.core.repositories.abstract_repository import AbstractRepository
from lab4.core.dto.dto import CardAccountDTO
from lab4.core.config import SERVER_IP, SERVER_PORT

class CardAccountRepository(AbstractRepository):
    __api_url: str = f"{SERVER_IP}:{SERVER_PORT}"

    def get_by_id(self, id: int) -> CardAccountDTO:
        response = requests.get(f"http://{self.__api_url}/accounts/{id}")
        if response.status_code == 200:
            json_card = response.json()
            return CardAccountDTO.parse_obj(json_card)
        else:
            return None
    
    def get_all(self) -> list[CardAccountDTO]:
        response = requests.get(f"http://{self.__api_url}/accounts")
        if response.status_code == 200:
            json_cards = response.json()
            cards = [CardAccountDTO.parse_obj(c) for c in json_cards]
            return cards
        else:
            return []
        
    def update(self, account: CardAccountDTO) -> None:
        requests.post(url=f"http://{self.__api_url}/accounts/{account.id}", data=account.json())

    def save(self):
        pass

    def delete(self):
        pass