"""
Registers all supported font codecs.
"""

from hinlegacy.decoder.registry import register_codec

from hinlegacy.decoder.devlys_010 import (
    FONT_SLUG as DEVLYS_SLUG,
    ALIASES as DEVLYS_ALIASES,
    decode as devlys_decode,
    encode as devlys_encode,
)
from hinlegacy.decoder.krutidev_010 import (
    FONT_SLUG as KRUTIDEV_SLUG,
    ALIASES as KRUTIDEV_ALIASES,
    decode as krutidev_decode,
    encode as krutidev_encode,
)
from hinlegacy.decoder.walkman_chanakya_905 import (
    FONT_SLUG as CHANAKYA_SLUG,
    ALIASES as CHANAKYA_ALIASES,
    decode as chanakya_decode,
    encode as chanakya_encode,
)


def register_all_codecs() -> None:
    register_codec(
        slug=DEVLYS_SLUG,
        aliases=DEVLYS_ALIASES,
        decode_fn=devlys_decode,
        encode_fn=devlys_encode,
    )
    register_codec(
        slug=KRUTIDEV_SLUG,
        aliases=KRUTIDEV_ALIASES,
        decode_fn=krutidev_decode,
        encode_fn=krutidev_encode,
    )
    register_codec(
        slug=CHANAKYA_SLUG,
        aliases=CHANAKYA_ALIASES,
        decode_fn=chanakya_decode,
        encode_fn=chanakya_encode,
    )