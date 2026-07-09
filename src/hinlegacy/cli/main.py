"""
Command-line interface for HinLegacy.
"""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="hinlegacy")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("detect")
    subparsers.add_parser("decode")
    subparsers.add_parser("auto")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    print(f"Command '{args.command}' will be implemented in Phase 4.")


if __name__ == "__main__":
    main()