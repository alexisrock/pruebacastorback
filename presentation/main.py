from http.client import HTTPException
from application.usescases.consultarArtista.artistarequest import ArtistaRequest
from application.usescases.consultarArtista.consultarartistaservice import ConsultarArtistaService
from domain.interfaces.servicespotify import AbstractSpotifyService
from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse
from application.dependency import get_consultar_artista_service, get_user_service
from application.dependency import get_login_service
from application.exceptions.apiexceptions import ApiException
from application.usescases.crearUsuario.userrequest import UserRequest
from application.usescases.crearUsuario.userservice import UserService
from application.usescases.login.loginservice import LoginService
from application.usescases.login.loginrequest import LoginRequest


# Crea una instancia de la aplicación FastAPI
app = FastAPI()



# Define un "path operation" (operación de ruta) para la URL raíz ("/")


# Otro ejemplo: una operación de ruta con un parámetro
@app.post("/user/create")
async def create(
    request: UserRequest,
    user_service: UserService = Depends(get_user_service)
):
    try:
        result = user_service.create(request)

        if result is None:
             # Aquí también, HTTPException espera argumentos posicionales
             raise HTTPException(
                status.HTTP_400_BAD_REQUEST, # Primer argumento: status_code
                "La operación de creación de usuario no devolvió un resultado válido."  
            )
        
        return JSONResponse(
                status_code=result.status,
                content={"message": result.message}
            )

    except ApiException as e:
        # ¡CAMBIO CLAVE AQUÍ!
        # Pasa status_code y detail como argumentos posicionales
        raise HTTPException(
            e.status,  # Primer argumento
            e.message  # Segundo argumento
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"Un error inesperado ocurrió: {e}"
        )



@app.post("/user/login")
async def login(
    request: LoginRequest,
    login_service: LoginService = Depends(get_login_service)
):
    try:
        result = login_service.login(request)

        if result is None:
             # Aquí también, HTTPException espera argumentos posicionales
             raise HTTPException(
                status.HTTP_400_BAD_REQUEST, # Primer argumento: status_code
                "La operación de login de usuario no devolvió un resultado válido." # Segundo argumento: detail
            )
        
        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result.model_dump()
            )

    except ApiException as e:
        # ¡CAMBIO CLAVE AQUÍ!
        # Pasa status_code y detail como argumentos posicionales
        raise HTTPException(
            e.status,  # Primer argumento
            e.message  # Segundo argumento
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"Un error inesperado ocurrió: {e}"
        )
        

@app.post("/artista/consultar")
async def consultar_artista(
    request: ArtistaRequest,
    consultar_service: ConsultarArtistaService = Depends(get_consultar_artista_service)
):
    try:
        result = consultar_service.consultar(request)

        if result is None:
             # Aquí también, HTTPException espera argumentos posicionales
             raise HTTPException(
                status.HTTP_400_BAD_REQUEST, # Primer argumento: status_code
                "La operación de creación de usuario no devolvió un resultado válido." # Segundo argumento: detail
            )
        
        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result.model_dump()
            )

    except ApiException as e:
        # ¡CAMBIO CLAVE AQUÍ!
        # Pasa status_code y detail como argumentos posicionales
        raise HTTPException(
            e.status,  # Primer argumento
            e.message  # Segundo argumento
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"Un error inesperado ocurrió: {e}"
        )
 

