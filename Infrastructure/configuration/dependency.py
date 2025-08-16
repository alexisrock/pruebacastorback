

from Infrastructure.persistence.consumorepositoryimpl import ConsumoRepositoryImpl
from Infrastructure.persistence.userrepositoryimpl import UserRepositoryImpl
from Infrastructure.service.spotifyserviceimpl import SpotifyServiceImpl
from domain.interfaces.consumorepository import ConsumoRepository
from domain.interfaces.userrepository import UserRepository
from domain.interfaces.servicespotify import AbstractSpotifyService

_spotify_service_instance = None

def get_user_repository() -> UserRepository:
    return UserRepositoryImpl()


def get_spotify_service() -> AbstractSpotifyService:
    global _spotify_service_instance
    if _spotify_service_instance is None:
        _spotify_service_instance = SpotifyServiceImpl()
    return _spotify_service_instance


def get_consumo_repository() -> ConsumoRepository:
    return ConsumoRepositoryImpl()