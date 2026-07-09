"""
Top-level public API for HinLegacy.
"""

from .models import ConversionResult


def convert(text: str, font: str | None = None) -> str:
    """
    Convert legacy-encoded text to Unicode Devanagari.
    If `font` is None, detection will be used (Phase 3+).
    """
    raise NotImplementedError("convert() will be implemented in Phase 4.")


def detect_and_convert(text: str) -> ConversionResult:
    """
    Detect the font used in `text` and convert it to Unicode Devanagari.
    """
    raise NotImplementedError("detect_and_convert() will be implemented in Phase 4.")