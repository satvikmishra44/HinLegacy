"""
Registry mapping font slugs/aliases to encoder/decoder functions.
"""

from collections.abc import Callable
from dataclasses import dataclass

from hinlegacy.exceptions import UnknownFontError


TextTransform = Callable[[str], str]


@dataclass(frozen=True)
class CodecEntry:
    slug: str
    decode: TextTransform
    encode: TextTransform


DECODER_REGISTRY: dict[str, CodecEntry] = {}


def _normalize_font_key(font: str) -> str:
    return font.strip().lower().replace("-", "_")


def register_codec(
    slug: str,
    aliases: tuple[str, ...],
    decode_fn: TextTransform,
    encode_fn: TextTransform,
) -> None:
    entry = CodecEntry(
        slug=slug,
        decode=decode_fn,
        encode=encode_fn,
    )

    keys = (slug, *aliases)
    for key in keys:
        normalized = _normalize_font_key(key)
        DECODER_REGISTRY[normalized] = entry


def resolve_codec(font: str) -> CodecEntry:
    normalized = _normalize_font_key(font)
    if normalized not in DECODER_REGISTRY:
        raise UnknownFontError(f"Unknown font: {font}")
    return DECODER_REGISTRY[normalized]