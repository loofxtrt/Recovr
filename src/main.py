import argparse
from spot.auth import change_prefix

def handle_prefix(old_prefix, new_prefix):
    change_prefix(old_prefix, new_prefix)

def create_parser():
    parser = argparse.ArgumentParser(description="Spotify playlist manager") # criação do parser principal
    subparsers = parser.add_subparsers(dest="command", required=True)        # criação do subparser

    # subcomando: prefix
    parser_prefix = subparsers.add_parser("prefix", help="Changes the prefix used to identify playlist tags")
    parser_prefix.add_argument("old_prefix")
    parser_prefix.add_argument("new_prefix")
    parser_prefix.set_defaults(func=lambda args: handle_prefix(args.old_prefix, args.new_prefix))

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
