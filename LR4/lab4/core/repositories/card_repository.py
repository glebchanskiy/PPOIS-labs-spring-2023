import requests

from lab4.core.repositories.abstract_repository import AbstractRepository
from lab4.core.dto.dto import CardDTO
from lab4.core.config import SERVER_IP, SERVER_PORT

class CardRepository(AbstractRepository):
    __api_url: str = f"{SERVER_IP}:{SERVER_PORT}"
    
    def get_by_id(self, id: int) -> CardDTO:
        response = requests.get(f"http://{self.__api_url}/cards/{id}")
        if response.status_code == 200:
            json_card = response.json()
            return CardDTO.parse_obj(json_card)
        else:
            return None
    
    def get_by_number(self, number: str) -> CardDTO:
        response = requests.get(f"http://{self.__api_url}/cards/by-number/{number}")
        if response.status_code == 200:
            json_card = response.json()
            return CardDTO.parse_obj(json_card)
        else:
            return None
    
    def get_all(self) -> list[CardDTO]:
        response = requests.get(f"http://{self.__api_url}/cards")
        if response.status_code == 200:
            json_cards = response.json()
            cards = [CardDTO.parse_obj(c) for c in json_cards]
            return cards
        else:
            return []
        
    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass