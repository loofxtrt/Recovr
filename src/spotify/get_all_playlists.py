from spotify.authorization import spot

def get_all_playlists(spot):
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