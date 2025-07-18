from pydantic import BaseModel

class ArtistaRequest(BaseModel):
  
  artistaname : str
