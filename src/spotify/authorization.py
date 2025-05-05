import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import reclog
from utils.extract_playlist_id import extract_playlist_id

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