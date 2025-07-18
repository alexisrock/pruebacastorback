from typing import Optional


class ArtistData:
    def __init__(self, id: str, name: str, genres: list, popularity: int, followers: int, image_url: Optional[str]):
        self.id = id
        self.name = name
        self.genres = genres
        self.popularity = popularity
        self.followers = followers
        self.image_url = image_url