import argparse

from spotify.authorization import spot
from commands.prefix import print_current_prefix, set_prefix
from commands.covers import covers

def create_parser():
    parser = argparse.ArgumentParser(description="Spotify playlist manager") # criação do parser principal
    subparsers = parser.add_subparsers(dest="command", required=True)        # criação do subparser

    # subcomando: prefix
    parser_prefix = subparsers.add_parser("prefix", help="Changes the prefix used to identify playlist tags")
    parser_prefix.add_argument("--set", type=str, help="New prefix")
    parser_prefix.set_defaults(func=handle_prefix)

    # subcomando: gray
    #parser_gray = subparsers.add_parser("gray", help="Converts the current playlist cover to a grayscale")
    #parser_gray.add_argument("url")
    #parser_gray.set_defaults(func=lambda args: cover_grayscale(spot, args.url))

    # subcomando: covers
    parser_covers = subparsers.add_parser("covers", help="Updates covers based on the playlists descriptions")
    parser_covers.set_defaults(func=lambda args: covers(spot))

    return parser

def handle_prefix(args):
    # se --set foi passado
    if args.set:
        set_prefix(spot, args.set)
    else:
        print_current_prefix()

def main():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args) # executa a função associada ao comando

if __name__ == "__main__":
    main()
