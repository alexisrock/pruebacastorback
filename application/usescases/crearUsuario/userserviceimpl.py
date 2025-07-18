from abc import abstractmethod
from application.commons.baseresponse import BaseResponse
from application.exceptions.apiexceptions import ApiException
from application.usescases.crearUsuario.userrequest import UserRequest
from application.usescases.crearUsuario.userservice import UserService
from fastapi import Depends
from Infrastructure.configuration.dependency import get_user_repository
from domain.entities.user import Users
from domain.interfaces.userrepository import UserRepository
import bcrypt

class UserServiceImpl(UserService):

    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
 


    
    def create(self, UserRequest: UserRequest) -> BaseResponse:   

        baseresponse = BaseResponse()

        try:

            users = Mapper.mapperuserrequesttouser(UserRequest)
            
            if users is None:
                raise ApiException("Error al crear mapear el usuario", 400)


            result = self.user_repository.create(users)
            
            if result == False:
                raise ApiException("Error al crear el usuario", 400)
        
            baseresponse.message = f"El usuario {UserRequest.name} fue creado con exito"
            baseresponse.status = 200

            return baseresponse
        except ApiException as e:
            raise ApiException(f"Error: {e.message}", e.status)
            
        except Exception as e:
            raise Exception(f"hubo un problema con {e}")
    


    


   
    
class Mapper:

    @staticmethod
    def mapperuserrequesttouser(userrequest: UserRequest, user_repository: UserRepository = Depends(get_user_repository))-> Users:

        if  userrequest is None:
            return None

        
        password  = Encript.hash_password(userrequest.password)

        users = Users(userrequest.name, userrequest.email, password.decode('utf-8'))
        return users


class Encript:

    @staticmethod
    def hash_password(password: str) -> bytes:
     
        salt = bcrypt.gensalt()       
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return hashed_password

    def verify_password(password: str, hashed_password: bytes) -> bool:       
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

