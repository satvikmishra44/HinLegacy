"""
HinLegacy
=========
Detect and decode legacy Hindi font encodings into Unicode Devanagari.
"""

__version__ = "0.1.0"

from .api import convert, detect_and_convert # Unified API for future
from .models import DetectionResult, ConversionResult # Individual submodules

__all__ = [
    "convert",
    "detect_and_convert",
    "DetectionResult",
    "ConversionResult",
]