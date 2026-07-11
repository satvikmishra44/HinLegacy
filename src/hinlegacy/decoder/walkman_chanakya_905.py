"""
Walkman Chanakya 905 decoder.
"""

from hinlegacy.decoder.engines.chanakya import chanakya_to_unicode, unicode_to_chanakya

FONT_SLUG = "walkman_chanakya_905"
DISPLAY_NAME = "Walkman Chanakya 905"
ALIASES = (
    "chanakya",
    "chanakya905",
    "walkman_chanakya",
    "walkman_chanakya_905",
    "walkman-chanakya905",
    "walkman-chanakya-905",
    "walkman"
)

def decode(text: str) -> str:
    return chanakya_to_unicode(text)

def encode(text: str) -> str:
    return unicode_to_chanakya(text)