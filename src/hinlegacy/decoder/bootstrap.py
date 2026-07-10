from hinlegacy.decoder.registry import register_decoder
from hinlegacy.decoder.devlys_010 import FONT_SLUG as DEVLYS_SLUG, ALIASES as DEVLYS_ALIASES, decode as devlys_decode
from hinlegacy.decoder.krutidev_010 import FONT_SLUG as KRUTIDEV_SLUG, ALIASES as KRUTIDEV_ALIASES, decode as krutidev_decode
from hinlegacy.decoder.walkman_chanakya_905 import FONT_SLUG as CHANAKYA_SLUG, ALIASES as CHANAKYA_ALIASES, decode as chanakya_decode

def register_all_decoders() -> None:
    register_decoder(DEVLYS_SLUG, DEVLYS_ALIASES, devlys_decode)
    register_decoder(KRUTIDEV_SLUG, KRUTIDEV_ALIASES, krutidev_decode)
    register_decoder(CHANAKYA_SLUG, CHANAKYA_ALIASES, chanakya_decode)