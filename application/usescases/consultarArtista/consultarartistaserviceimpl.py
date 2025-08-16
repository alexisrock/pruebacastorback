from application.usescases.consultarArtista.consultarartistaservice import ConsultarArtistaService
from application.usescases.consultarArtista.artistarequest import ArtistaRequest
from application.usescases.consultarArtista.artistaresponse import ArtistaResponse
from domain.interfaces.consumorepository import ConsumoRepository
from domain.interfaces.servicespotify import AbstractSpotifyService
from application.exceptions.apiexceptions import ApiException
from Infrastructure.persistence.consumorepositoryimpl import ConsumoRepositoryImpl
import json

class ConsultarArtistaServiceImpl(ConsultarArtistaService):
    def __init__(self, spotify_service: AbstractSpotifyService, consumo_repository: ConsumoRepository):
        self.spotify_service = spotify_service
        self.consumo_repository = consumo_repository

    def consultar(self, request: ArtistaRequest) -> ArtistaResponse:
        try:
       
            consumo = self.consumo_repository.get_consumo_by_artistname(request.artistaname)
            if consumo and consumo.respuestajson:
                try:
                    data = json.loads(consumo.respuestajson)
                    return ArtistaResponse(
                        id=data['id'],
                        name=data['name'],
                        genres=data['genres'],
                        popularity=data['popularity'],
                        followers=data['followers'],
                        image_url=data['image_url']
                    )
                except Exception as e:
                    print(f"Error al deserializar RespuestaJson: {e}")
                    # Si hay error en el json, sigue con el consumo normal
           
            artist_data = self.spotify_service.get_data(request.artistaname)
            if artist_data is None:
                raise ApiException("No se encontró información para el artista solicitado.", 404)
            # Mapear a ArtistaResponse
            response = ArtistaResponse(
                id=artist_data.id,
                name=artist_data.name,
                genres=artist_data.genres,
                popularity=artist_data.popularity,
                followers=artist_data.followers,
                image_url=artist_data.image_url
            )
            # Guardar el resultado en la tabla Consumos
            try:
                self.consumo_repository.insert_consumo(
                    artistname=request.artistaname,
                    respuestajson=json.dumps(response.__dict__)
                )
            except Exception as e:
                print(f"Error al guardar el consumo: {e}")
            return response
        except Exception as e:
            if isinstance(e, ApiException):
                raise
            raise ApiException(f"Error al consultar el artista: {str(e)}", 404)
