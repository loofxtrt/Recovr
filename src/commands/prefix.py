from utils import reclog
from spotify.get_all_playlists import get_all_playlists

def prefix(spot, old_prefix, new_prefix):
    playlists = get_all_playlists(spot=spot)

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