from hinlegacy.decoder.bootstrap import register_all_decoders
from hinlegacy.decoder.dispatch import decode_text

register_all_decoders()

__all__ = ["decode_text"]