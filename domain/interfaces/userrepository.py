from abc import ABC, abstractmethod
from domain.entities.user import Users

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: Users) -> bool:      
        pass

    @abstractmethod
    def login(self, email: str) -> Users:      
        pass
