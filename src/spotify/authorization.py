import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from utils import reclog
from utils.extract_playlist_id import extract_playlist_id

# carregar dotenv
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# credenciais
client_id = SPOTIFY_CLIENT_ID         # identifica o app
client_secret = SPOTIFY_CLIENT_SECRET # "senha" do app
redirect_uri = "https://example.com"  # página pra onde o usuário vai ser redirecionado depois da autorização

# permissões
scope = "playlist-read-private playlist-modify-public playlist-modify-private ugc-image-upload"

# criação do objeto e autenticação. quando o código é rodado pela primeira vez, uma página do spotify abre pra autorizar o app
spot = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))