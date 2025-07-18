from pydantic import BaseModel

class TokenResponse(BaseModel):

    token: bool
    name: str


 
