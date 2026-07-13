"""
Command-line interface for HinLegacy.
"""

from __future__ import annotations

import argparse
from typing import Sequence

from hinlegacy.decoder import decode_text, encode_text, list_supported_fonts
from hinlegacy.detector import detect_font
from hinlegacy.exceptions import DetectionFailedError, HinLegacyError, UnknownFontError


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hinlegacy",
        description="Detect, decode, and encode legacy Hindi font text.",
        epilog="Use 'hinlegacy <command> -h' to see help for a specific command.",
    )

    subparsers = parser.add_subparsers(dest="command")

    detect_parser = subparsers.add_parser(
        "detect",
        help="Detect the legacy font used in the given text.",
    )
    detect_parser.add_argument("text", help="Legacy font text to analyze.")
    detect_parser.set_defaults(func=_run_detect)

    decode_parser = subparsers.add_parser(
        "decode",
        help="Decode legacy font text into Unicode Hindi.",
    )
    decode_parser.add_argument("text", help="Legacy font text to decode.")
    decode_parser.add_argument(
        "--font",
        required=True,
        help="Font slug or alias, for example: krutidev_010, devlys_010, walkman_chanakya_905.",
    )
    decode_parser.set_defaults(func=_run_decode)

    encode_parser = subparsers.add_parser(
        "encode",
        help="Encode Unicode Hindi text into a legacy font.",
    )
    encode_parser.add_argument("text", help="Unicode Hindi text to encode.")
    encode_parser.add_argument(
        "--font",
        required=True,
        help="Target font slug or alias, for example: krutidev_010, devlys_010, walkman_chanakya_905.",
    )
    encode_parser.set_defaults(func=_run_encode)

    convert_parser = subparsers.add_parser(
        "convert",
        help="Convert text to Unicode by auto-detecting the font, or by using the supplied font.",
    )
    convert_parser.add_argument("text", help="Input text to convert.")
    convert_parser.add_argument(
        "--font",
        help="Optional known font slug or alias. If omitted, HinLegacy will auto-detect the font.",
    )
    convert_parser.set_defaults(func=_run_convert)

    list_fonts_parser = subparsers.add_parser(
        "list-fonts",
        help="List all supported fonts.",
    )
    list_fonts_parser.set_defaults(func=_run_list_fonts)

    return parser


def _run_detect(args: argparse.Namespace) -> int:
    result = detect_font(args.text)
    print(result.font_slug)
    print(f"confidence: {result.confidence:.2f}")
    print(f"method: {result.method}")
    return 0


def _run_decode(args: argparse.Namespace) -> int:
    output = decode_text(args.text, args.font)
    print(output)
    return 0


def _run_encode(args: argparse.Namespace) -> int:
    output = encode_text(args.text, args.font)
    print(output)
    return 0


def _run_convert(args: argparse.Namespace) -> int:
    if args.font:
        output = decode_text(args.text, args.font)
        print(output)
        return 0

    detection = detect_font(args.text)
    output = decode_text(args.text, detection.font_slug)
    print(output)
    return 0


def _run_list_fonts(args: argparse.Namespace) -> int:
    for font in list_supported_fonts():
        print(font)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "func"):
        parser.print_help()
        return 1

    try:
        return args.func(args)
    except UnknownFontError as exc:
        print(f"Error: {exc}")
        return 2
    except DetectionFailedError as exc:
        print(f"Detection failed: {exc}")
        return 3
    except HinLegacyError as exc:
        print(f"HinLegacy error: {exc}")
        return 4