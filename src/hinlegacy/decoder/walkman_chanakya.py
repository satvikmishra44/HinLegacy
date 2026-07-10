"""
Walkman Chanakya decoder.
"""
from chanakya import chanakya_to_unicode

FONT_SLUG = "walkman_chanakya"
DISPLAY_NAME = "Walkman Chanakya"
ALIASES = ("chanakya", "walkman-chanakya905")


def decode(text: str) -> str:
    return chanakya_to_unicode(text)