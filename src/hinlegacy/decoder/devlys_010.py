"""
DevLys 010 decoder.
"""

from devlys import devlys_to_unicode

FONT_SLUG = "devlys_010"
DISPLAY_NAME = "DevLys 010"
ALIASES = ("devlys", "devlys010", "dev-lys-010", "devlys-010")


def decode(text: str) -> str:
    return devlys_to_unicode(text)