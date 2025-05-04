import argparse

from spotipy.auth import get_album_covers_urls

def generate_grid(link, size):
    # obter o id da playlist a partir do link
    playlist_id = link.split("/")[-1].split("?")[0]

    covers_urls = get_album_covers_urls(playlist_id, size)

# definição dos parsers
parser = argparse.ArgumentParser(description="Playlist cover generator") # criação do parser principal
subparsers = parser.add_subparsers(dest="result", required=True)         # criação do grupo de subcomandos

# subcomando grid
parser_grid = subparsers.add_parser("grid", help="Generates a grid with the album covers inside the playlist")
parser_grid.add_argument("link", help="Link to the playlist")
parser_grid.add_argument("grid", type=int, help="How many covers per row and column")

# definir a função a ser chamada pra esse comando
parser_grid.set_defaults(func=generate_grid)

# receber os argumentos
args = parser.parse_args()      # interpretar os argumentos
args.func(args.link, args.size) # chamar a função correspondente ao subcomando e passar os argumentos