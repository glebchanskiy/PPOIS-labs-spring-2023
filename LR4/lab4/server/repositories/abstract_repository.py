from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete_by_id(self):
        pass