from abc import ABC, abstractmethod
from application.usescases.login.tokenresponse import TokenResponse
from application.usescases.login.loginrequest import LoginRequest

class LoginService(ABC):

    @abstractmethod
    def login(self, request: LoginRequest) -> TokenResponse:  
        pass 

