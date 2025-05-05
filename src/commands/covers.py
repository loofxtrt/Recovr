from utils import reclog
from utils.prefix_settings import get_current_prefix
from spotify.get_all_playlists import get_all_playlists
from spotify.processing.cover_apply_manipulation import cover_apply_manipulation

def covers(spot):
    playlists = get_all_playlists(spot)
    prefix = get_current_prefix()

    for playlist in playlists:
        # obter os valores da playlist
        playlist_id = playlist['id']
        description = playlist.get('description', '')

        if not description.strip():
            continue
        
        # checar por instruções seguidas de prefixos na descrição da playlist
        if f"cover{prefix}gray" in description:
            cover_apply_manipulation(spot, playlist_id, "grayscale")
            
            reclog.info((f"Cover updated for {playlist['name']}", "green"))