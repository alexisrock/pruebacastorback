class ApiException(Exception):
    def __init__(self, message: str, status: int):
        super().__init__(message) # Llama al constructor de la clase base Exception
        self.message = message   # Guarda el mensaje como un atributo
        self.status = status   
        