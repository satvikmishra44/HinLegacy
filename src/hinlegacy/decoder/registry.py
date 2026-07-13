"""
Registry mapping font slugs/aliases to encoder/decoder functions.
"""

from __future__ import annotations

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
    normalized = font.strip().lower().replace("-", "_")
    if not normalized:
        raise UnknownFontError("Font name cannot be empty.")
    return normalized


def register_codec(
    slug: str,
    aliases: tuple[str, ...],
    decode_fn: TextTransform,
    encode_fn: TextTransform,
) -> None:
    normalized_slug = _normalize_font_key(slug)

    entry = CodecEntry(
        slug=normalized_slug,
        decode=decode_fn,
        encode=encode_fn,
    )

    keys = (slug, *aliases)
    for key in keys:
        normalized = _normalize_font_key(key)
        DECODER_REGISTRY[normalized] = entry


def resolve_codec(font: str) -> CodecEntry:
    normalized = _normalize_font_key(font)
    try:
        return DECODER_REGISTRY[normalized]
    except KeyError as exc:
        available = ", ".join(list_supported_fonts())
        raise UnknownFontError(
            f"Unknown font: {font}. Supported fonts: {available}"
        ) from exc


def is_supported_font(font: str) -> bool:
    try:
        normalized = _normalize_font_key(font)
    except UnknownFontError:
        return False
    return normalized in DECODER_REGISTRY


def list_supported_fonts() -> list[str]:
    return sorted({entry.slug for entry in DECODER_REGISTRY.values()})