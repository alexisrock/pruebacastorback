from abc import ABC, abstractmethod
from application.usescases.consultarArtista.artistarequest import ArtistaRequest
from application.usescases.consultarArtista.artistaresponse import ArtistaResponse




class ConsultarArtistaService(ABC):
    @abstractmethod
    def consultar(self, request: ArtistaRequest) -> ArtistaResponse:
        pass
