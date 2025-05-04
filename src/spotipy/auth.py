import spotipy
from spotipy.oauth2 import SpotifyOAuth

# credenciais
client_id = "09e03a12d3494e0faa7e341bcf01d175"     # identifica o app
client_secret = "57e071036d11471789d23232759972c3" # "senha" do app
redirect_uri = "https://example.com"               # página pra onde o usuário vai ser redirecionado depois da autorização

# permissões
scope = "playlist-modify-public playlist-modify-private"

# criação do objeto e autenticação. quando o código é rodado, uma página do spotify abre pra autorizar o app
spot = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

def get_album_covers_urls(playlist_id, limit):
    if not playlist_id or not limit:
        return

    # definição da playlist e de quantas capas vão ser retornadas
    tracks = spot.playlist_tracks(playlist_id=playlist_id, limit=limit)
    cover_urls = []

    # pegar a primeira imagem do album de cada track
    for track in tracks['items']:
        album_cover = track['track']['album']['images'][0]['url']
        cover_urls.append(album_cover)

    return cover_urls