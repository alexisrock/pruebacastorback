from abc import ABC, abstractmethod
from application.commons.baseresponse import BaseResponse
from application.usescases.crearUsuario.userrequest import UserRequest


class UserService(ABC):

    @abstractmethod
    def create(self, user: UserRequest) -> BaseResponse:      
        pass
    