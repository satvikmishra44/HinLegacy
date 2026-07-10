"""
Registry mapping font slugs/aliases to decoder functions.
"""

from collections.abc import Callable

DECODER_REGISTRY: dict[str, Callable[[str], str]] = {}


def register_decoder(slug: str, aliases: tuple[str, ...], decode_fn: Callable[[str], str]) -> None:
    keys = (slug, *aliases)
    for key in keys:
        normalized = key.strip().lower().replace("-", "_")
        DECODER_REGISTRY[normalized] = decode_fn

def resolve_decoder(font: str) -> Callable[[str], str]:
    normalized = font.strip().lower().replace("-", "_")
    if normalized not in DECODER_REGISTRY:
        available = ", ".join(sorted(DECODER_REGISTRY))
        raise KeyError(f"Unknown font: {font}. Available fonts/aliases: {available}")
    return DECODER_REGISTRY[normalized]