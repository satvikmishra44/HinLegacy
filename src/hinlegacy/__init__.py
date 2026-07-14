"""
HinLegacy public package interface.
"""

from hinlegacy.api import convert, decode, detect, encode
from hinlegacy.models import ConversionResult, DetectionResult

__version__ = "1.0.0"

__all__ = [
    "detect",
    "decode",
    "encode",
    "convert",
    "DetectionResult",
    "ConversionResult",
]