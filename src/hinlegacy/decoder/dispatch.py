"""
Dispatches encoding/decoding to the correct font-specific codec.
"""

from hinlegacy.decoder.registry import resolve_codec


def decode_text(text: str, font: str) -> str:
    codec = resolve_codec(font)
    return codec.decode(text)


def encode_text(text: str, font: str) -> str:
    codec = resolve_codec(font)
    return codec.encode(text)