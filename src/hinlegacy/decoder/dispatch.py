"""
Dispatches decoding to the correct font-specific decoder.
"""

from hinlegacy.decoder.registry import resolve_decoder

def decode_text(text: str, font: str) -> str:
    decoder  = resolve_decoder(font)
    return decoder(text)