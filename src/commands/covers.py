from utils import reclog
from utils.prefix_settings import get_current_prefix
from spotify.get_all_playlists import get_all_playlists
from spotify.processing.cover_manipulation import stack, apply

def covers(spot):
    playlists = get_all_playlists(spot)
    prefix = get_current_prefix()

    for playlist in playlists:
        new_cover = None

        # obter os valores da playlist
        playlist_id = playlist['id']
        description = playlist.get('description', '')

        if not description.strip():
            continue
        
        # checar por instruções seguidas de prefixos na descrição da playlist
        if f"cover{prefix}gray" in description:
            new_cover = stack(spot, playlist_id, "grayscale")

        # ISSO AQUI É UM PERIGO (adiciona textos nas capas sem salvar a versão anterior, então não tem backup)
        #type_map = {
        #    "type:genre": ("gen", "#e00003"),
        #    "type:collection": ("col", "#f5db00"),
        #    "type:soundslike": ("sol", "#293deb"),
        #    "type:media": ("med", "#f564b0")
        #}
        #for key in type_map:
        #    if key in description:
        #        label, color = type_map[key]
        #        new_cover = stack(spot, playlist_id, "text", text=label, color=color)

        # aplicação
        if new_cover is not None:
            apply(spot=spot, playlist_id=playlist_id, cover=new_cover)
            reclog.info((f"Cover updated for {playlist['name']}", "green"))