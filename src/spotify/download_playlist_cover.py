import requests
from PIL import Image
from io import BytesIO

import spotipy

def download_playlist_cover(spot, playlist_id):
    # buscar pela capa da playlist indicada e retornar caso não ache
    covers = spot.playlist_cover_image(playlist_id=playlist_id)
    if not covers:
        return None

    # pegar a url da primeira capa retornada e baixar ela, abrindo a imagem com o pillow
    url = covers[0]['url']
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGBA") # .convert("RGBA") serve pra remover o jpeg até a hora da aplicação na playlist de novo

    return image