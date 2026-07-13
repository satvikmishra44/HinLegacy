"""
Top-level public API for HinLegacy.
"""

from __future__ import annotations

from hinlegacy.decoder import decode_text, encode_text
from hinlegacy.detector import detect_font
from hinlegacy.models import ConversionResult, DetectionResult


def detect(text: str) -> DetectionResult:
    """
    Detect the legacy Hindi font used in the given text.

    Args:
        text: Legacy-encoded input text.

    Returns:
        DetectionResult containing font slug, confidence, and method.
    """
    return detect_font(text)


def decode(text: str, font: str) -> str:
    """
    Decode legacy Hindi text into Unicode using the specified font.

    Args:
        text: Legacy-encoded input text.
        font: Font slug or alias.

    Returns:
        Decoded Unicode text.
    """
    return decode_text(text, font)


def encode(text: str, font: str) -> str:
    """
    Encode Unicode Hindi text into the specified legacy font.

    Args:
        text: Unicode Hindi input text.
        font: Target font slug or alias.

    Returns:
        Encoded legacy-font text.
    """
    return encode_text(text, font)


def convert(text: str, font: str | None = None) -> ConversionResult:
    """
    Convert legacy Hindi text into Unicode.

    If font is provided, decoding is done directly using that font.
    If font is omitted, the font is detected automatically first.

    Args:
        text: Legacy-encoded input text.
        font: Optional font slug or alias.

    Returns:
        ConversionResult containing the decoded Unicode text and metadata.
    """
    if font is not None:
        unicode_text = decode_text(text, font)
        return ConversionResult(
            unicode_text=unicode_text,
            detected_font=font,
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