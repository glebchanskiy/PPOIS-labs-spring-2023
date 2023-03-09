from abc import ABC
from abc import abstractmethod

class Engine(ABC):
    def __init__(self, path) -> None:
        super().__init__()
        self._path = path

    @abstractmethod
    def deserialize(self) -> dict:
        pass
    
    @abstractmethod
    def serialize(self, data: dict) -> None:
        pass
        
