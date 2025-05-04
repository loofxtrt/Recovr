import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import reclog

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

def change_prefix(old_prefix, new_prefix):
    playlists = spot.current_user_playlists(limit=50)

    for playlist in playlists['items']:
        playlist_id = playlist['id']
        description = playlist.get('description', '')

        reclog.info(f"Checking for {playlist['name']}")
        
        if description == None:
            reclog.info("No description found, moving on")
            return
        
        reclog.info(f"Current description: {description}")

        if old_prefix in description:
            new_description = description.replace(old_prefix, new_prefix)
            spot.playlist_change_details(playlist_id=playlist_id, description=new_description)
            
            reclog.info(f"Prefix for {playlist['name']} changed {old_prefix} ---> {new_prefix}")
        else:
            reclog.info(f"Old prefix not found in {playlist['name']}, moving on")