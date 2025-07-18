import os
import requests
from typing import Optional
from domain.entities.artistdata import ArtistData
from domain.interfaces.servicespotify import AbstractSpotifyService
from dotenv import load_dotenv


class SpotifyServiceImpl(AbstractSpotifyService):
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.api_url = 'https://api.spotify.com/v1/search'
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:

        if not self.client_id or not self.client_secret:
            raise ValueError("SPOTIFY_CLIENT_ID y SPOTIFY_CLIENT_SECRET deben estar definidos en las variables de entorno")
        response = requests.post(
            self.token_url,
            data={'grant_type': 'client_credentials'},
            auth=(self.client_id, self.client_secret)
        )
        response.raise_for_status()
       
        return response.json()['access_token']

    def get_data(self, artist: str) -> Optional[ArtistData]:
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {'q': artist, 'type': 'artist', 'limit': 1}
        response = requests.get(self.api_url, headers=headers, params=params)
        if response.status_code != 200:
            return None
        data = response.json()
    
        items = data.get('artists', {}).get('items', [])
        if not items:
            return None
        artist_info = items[0]
        return ArtistData(
            id=artist_info['id'],
            name=artist_info['name'],
            genres=artist_info.get('genres', []),
            popularity=artist_info.get('popularity', 0),
            followers=artist_info.get('followers', {}).get('total', 0),
            image_url=artist_info.get('images', [{}])[0].get('url') if artist_info.get('images') else None
        )
