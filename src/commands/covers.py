from utils import reclog
from spotify.get_all_playlists import get_all_playlists
from spotify.processing.cover_apply_manipulation import cover_apply_manipulation

def covers(spot):
    playlists = get_all_playlists(spot)

    for playlist in playlists:
        playlist_id = playlist['id']
        description = playlist.get('description', '')

        if not description.strip():
            continue

        if "cover:gray" in description:
            cover_apply_manipulation(spot, playlist_id, "grayscale")
            
            reclog.info((f"Cover updated for {playlist['name']}", "green"))