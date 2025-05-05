def extract_id(url):
    # exemplo de link: https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
    # o id é 37i9dQZF1DXcBWIGoYBM5M
    playlist_id = url.split('/')[-1].split('?')[0]
    return playlist_id