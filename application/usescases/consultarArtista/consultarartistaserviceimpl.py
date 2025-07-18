from application.usescases.consultarArtista.consultarartistaservice import ConsultarArtistaService
from application.usescases.consultarArtista.artistarequest import ArtistaRequest
from application.usescases.consultarArtista.artistaresponse import ArtistaResponse
from domain.interfaces.servicespotify import AbstractSpotifyService
from application.exceptions.apiexceptions import ApiException

class ConsultarArtistaServiceImpl(ConsultarArtistaService):

    def __init__(self, spotify_service: AbstractSpotifyService):
        self.spotify_service = spotify_service  

    
    def consultar(self, request: ArtistaRequest) -> ArtistaResponse:
        try:
            artist_data = self.spotify_service.get_data(request.artistaname)
            if artist_data is None:
                raise ApiException("No se encontró información para el artista solicitado.", 404)
            return ArtistaResponse(
                id=artist_data.id,
                name=artist_data.name,
                genres=artist_data.genres,
                popularity=artist_data.popularity,
                followers=artist_data.followers,
                image_url=artist_data.image_url
            )
        except Exception as e:
            if isinstance(e, ApiException):
                raise
            raise ApiException(f"Error al consultar el artista: {str(e)}", 404)
