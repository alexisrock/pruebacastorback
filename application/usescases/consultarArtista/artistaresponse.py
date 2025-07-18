
from typing import List, Optional
from pydantic import BaseModel



class ArtistaResponse(BaseModel):

    id: str
    name: str
    genres: List[str]
    popularity: int
    followers: int
    image_url: str