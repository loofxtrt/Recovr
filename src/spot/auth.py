import requests
import base64
from PIL import Image
from io import BytesIO

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import reclog
from utils.extract_id import extract_id
from pillow.grayscale import grayscale

# credenciais
client_id = "09e03a12d3494e0faa7e341bcf01d175"     # identifica o app
client_secret = "57e071036d11471789d23232759972c3" # "senha" do app
redirect_uri = "https://example.com"               # página pra onde o usuário vai ser redirecionado depois da autorização

# permissões
scope = "playlist-read-private playlist-modify-public playlist-modify-private ugc-image-upload"

# criação do objeto e autenticação. quando o código é rodado pela primeira vez, uma página do spotify abre pra autorizar o app
spot = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

def download_playlist_cover(playlist_id):
    covers = spot.playlist_cover_image(playlist_id=playlist_id)
    if not covers:
        return None

    url = covers[0]['url']
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    return image

def get_all_playlists():
    playlists = []
    limit = 50
    offset = 0

    # continuar buscando por playlists até que o spotify não retorne mais nenhuma
    # offset é quantos resultados ele deve pular pra próxima busca, então vai de 50 em 50
    while True:
        response = spot.current_user_playlists(limit=limit, offset=offset)
        items = response['items']

        # parar de requisitar playlists caso mais nenhuma seja encontrada
        if not items:
            break
        
        # resultados
        playlists.extend(items) # adicionar os itens à lista
        offset += limit # passar pra próxima página
    
    return playlists

def change_prefix(old_prefix, new_prefix):
    playlists = get_all_playlists()

    for playlist in playlists:
        # obter os valores da playlist
        playlist_id = playlist['id']
        playlist_name = playlist['name']
        description = playlist.get('description', '')

        reclog.info((f"Checking for {playlist_name}", "green bold"))
        
        if not description.strip():
            reclog.info("No description found, moving on")
            continue
        
        reclog.info(f"Current description: {description}")

        # substituir o prefixo antigo na descrição caso ele tenha sido encontrado nela
        if old_prefix in description:
            new_description = description.replace(old_prefix, new_prefix)
            spot.playlist_change_details(playlist_id=playlist_id, description=new_description)
            
            reclog.info((f"Prefix for {playlist_name} changed:", "green"), f"{old_prefix} {new_prefix}")
            reclog.info(f"New description: {new_description}")
        else:
            reclog.info(f"Old prefix not found in {playlist_name}, moving on")

def cover_grayscale(playlist_url):
    playlist_id = extract_id(playlist_url) # extrair o id da url da playlist
    buffer = BytesIO() # buffer pra salvar temporariamente a imagem

    # baixar a capa da playlist e converter pra grayscale
    cover = grayscale(download_playlist_cover(playlist_id=playlist_id))
    cover.save(buffer, format='JPEG')

    # fallback
    data_bytes = buffer.getvalue()
    if len(data_bytes) > 256000:
        raise ValueError("Image exceeds 256KB")

    # passar a imagem pra base64 e aplicar na playlist
    cover_64 = base64.b64encode(data_bytes).decode('utf-8')
    spot.playlist_upload_cover_image(playlist_id=playlist_id, image_b64=cover_64)