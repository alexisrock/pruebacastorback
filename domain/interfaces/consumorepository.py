from abc import ABC, abstractmethod

class ConsumoRepository(ABC):
    @abstractmethod
    def insert_consumo(self, artistname: str, respuestajson: str):
        pass

    @abstractmethod
    def get_consumo_by_artistname(self, artistname: str):
        pass