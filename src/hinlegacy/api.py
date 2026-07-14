"""
Top-level public API for HinLegacy.
"""

from __future__ import annotations

from hinlegacy.decoder import decode_text, encode_text
from hinlegacy.decoder.registry import resolve_codec
from hinlegacy.detector import detect_font
from hinlegacy.models import ConversionResult, DetectionResult


def detect(text: str) -> DetectionResult:
    """
    Detect the legacy Hindi font used in the given text.
    """
    return detect_font(text)


def decode(text: str, font: str) -> str:
    """
    Decode legacy Hindi text into Unicode using the specified font.
    """
    return decode_text(text, font)


def encode(text: str, font: str) -> str:
    """
    Encode Unicode Hindi text into the specified legacy font.
    """
    return encode_text(text, font)


def convert(text: str, font: str | None = None) -> ConversionResult:
    """
    Convert legacy Hindi text into Unicode.

    If font is provided, decoding is done directly using that font.
    If font is omitted, the font is detected automatically first.
    """
    if font is not None:
        codec = resolve_codec(font)
        unicode_text = codec.decode(text)
        return ConversionResult(
            unicode_text=unicode_text,
            detected_font=codec.slug,
            confidence=1.0,
            detection_method="user_supplied",
        )

    detection = detect_font(text)
    unicode_text = decode_text(text, detection.font_slug)

    return ConversionResult(
        unicode_text=unicode_text,
        detected_font=detection.font_slug,
        confidence=detection.confidence,
        detection_method=detection.method,
    )