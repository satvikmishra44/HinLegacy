"""
KrutiDev 010 decoder.
"""

from hinlegacy.decoder.engines.krutidev import krutidev_to_unicode, unicode_to_krutidev

FONT_SLUG = "krutidev_010"
DISPLAY_NAME = "KrutiDev 010"
ALIASES = ("krutidev", "krutidev010", "kruti-dev-010", "krutidev-010")


def decode(text: str) -> str:
    return krutidev_to_unicode(text)

def encode(text: str) -> str:
    return unicode_to_krutidev(text)