"""
Registry mapping font slugs/aliases to decoder functions.
"""

DECODER_REGISTRY: dict = {}


def register_decoder(slug: str, aliases: tuple, decode_fn) -> None:
    DECODER_REGISTRY[slug] = decode_fn
    for alias in aliases:
        DECODER_REGISTRY[alias] = decode_fn


def resolve_decoder(font: str):
    if font not in DECODER_REGISTRY:
        raise KeyError(f"Unknown font: {font}")
    return DECODER_REGISTRY[font]