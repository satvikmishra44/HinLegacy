from hinlegacy.decoder.bootstrap import register_all_codecs
from hinlegacy.decoder.dispatch import decode_text, encode_text
from hinlegacy.decoder.registry import is_supported_font, list_supported_fonts

register_all_codecs()

__all__ = [
    "decode_text",
    "encode_text",
    "is_supported_font",
    "list_supported_fonts",
]