from Infrastructure.configuration.dependency import get_user_repository
from application.usescases.login.tokenresponse import TokenResponse
from application.usescases.login.loginrequest import LoginRequest
from application.usescases.crearUsuario.userserviceimpl import Encript
from application.usescases.login.loginservice import LoginService
from domain.interfaces.userrepository import UserRepository
from application.exceptions.apiexceptions import ApiException


class LoginServiceImpl(LoginService):



    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def login(self, request: LoginRequest) -> TokenResponse:  
     
        try:

            if not self.validation(request.email,request.password):
                raise ApiException("Error en el request existe campos vacios", 400)
 
            user = self.user_repository.login(request.email)
            print("user", user)

            if user is None:
                 raise ApiException("El correo es invalido", 400)
            
            hash_pass = user.password.encode('utf-8')
            if not Encript.verify_password(request.password,  hash_pass):
                raise ApiException("La contraseña es incorrecta", 400)

 


            return TokenResponse(token=True, name=user.name)

        except ApiException as e:
            raise ApiException(f"Error: {e.message}", e.status)
            
        except Exception as e:
            raise Exception(f"hubo un problema con {e}")


    def validation(self, email: str, password: str)->bool:

        if email == "" or password == "":
            return False

        return True 