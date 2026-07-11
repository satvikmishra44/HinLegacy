from hinlegacy.decoder.bootstrap import register_all_codecs
from hinlegacy.decoder.dispatch import decode_text, encode_text

register_all_codecs()

__all__ = ["decode_text", "encode_text"]