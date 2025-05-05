import json
from html import unescape

from utils import reclog
from utils.prefix_settings import get_current_prefix, write_new_prefix
from spotify.get_all_playlists import get_all_playlists

def print_current_prefix():
    prefix = get_current_prefix()
    reclog.info(f"Your current prefix is {prefix}")

def set_prefix(spot, new_prefix):
    """
    muda o prefixo atual, e também checa todas as descrições de todas as playlists
    pra encontrar os lugares onde o prefixo antigo é usado e substituir ele
    """
    # checar pelo prefixo antigo, e se ele for diferente do novo, iniciar a função
    old_prefix = get_current_prefix()
    if old_prefix == new_prefix:
        reclog.info("New prefix is the same as the old one, prefix not changed")
        return

    playlists = get_all_playlists(spot=spot)
    
    # número de prefixos que realmente foram mudados,
    # previnindo que o prefixo mude no código, mas no spotify, por algum problema da api, não
    affected = 0

    for playlist in playlists:
        # obter os valores da playlist
        playlist_id = playlist['id']
        playlist_name = playlist['name']
        description = playlist.get('description', '')

        # garantir que os prefixos não sejam escapados acidentalmente, tipo &amp ao invés de &
        description = unescape(description)

        reclog.info((f"Checking for {playlist_name}", "green bold"))
        
        if not description.strip():
            reclog.info("No description found, moving on")
            continue
        
        reclog.info(f"Current description: {description}")

        # substituir o prefixo antigo na descrição caso ele tenha sido encontrado nela
        if old_prefix in description:
            new_description = description.replace(old_prefix, new_prefix)
            spot.playlist_change_details(playlist_id=playlist_id, description=new_description)
            
            reclog.info((f"Prefix for {playlist_name} changed:", "green"), f"{old_prefix} ---> {new_prefix}")
            reclog.info(f"New description: {new_description}")

            affected += 1
        else:
            reclog.info(f"Old prefix not found in {playlist_name}, moving on")
        
    # redefinir o prefixo após fazer a checagem e substituição
    if affected > 0:
        write_new_prefix(new_prefix=new_prefix)
    else:
        reclog.info(("No changes were made to any playlist descriptions, prefix not changed", "green"))