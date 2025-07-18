from abc import ABC, abstractmethod

class AbstractSpotifyService(ABC):
    @abstractmethod
    def get_data(self, artist: str):       
        pass
