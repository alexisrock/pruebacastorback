


from application.usescases.consultarArtista.consultarartistaservice import ConsultarArtistaService
from application.usescases.consultarArtista.consultarartistaserviceimpl import ConsultarArtistaServiceImpl
from application.usescases.crearUsuario.userservice import UserService
from application.usescases.crearUsuario.userserviceimpl import UserServiceImpl
from domain.interfaces.servicespotify import AbstractSpotifyService
from domain.interfaces.userrepository import UserRepository
from Infrastructure.configuration.dependency import  get_spotify_service, get_user_repository
from fastapi import Depends
from application.usescases.login.loginservice import LoginService
from application.usescases.login.loginserviceimpl import LoginServiceImpl


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserServiceImpl(user_repository=user_repository)


def get_login_service(user_repository: UserRepository = Depends(get_user_repository)) -> LoginService:
    return LoginServiceImpl(user_repository=user_repository)

def get_consultar_artista_service(spotify_service: AbstractSpotifyService = Depends(get_spotify_service)) -> ConsultarArtistaService:
    return ConsultarArtistaServiceImpl(spotify_service=spotify_service)