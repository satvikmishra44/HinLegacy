"""
HinLegacy public package interface.
"""

version = 0.5

from hinlegacy.api import convert, decode, detect, encode
from hinlegacy.models import ConversionResult, DetectionResult

__all__ = [
    "detect",
    "decode",
    "encode",
    "convert",
    "DetectionResult",
    "ConversionResult",
]