"""
Custom exceptions for HinLegacy.
"""


class HinLegacyError(Exception):
    """Base exception for all HinLegacy errors."""


class UnknownFontError(HinLegacyError):
    """Raised when a font slug or alias cannot be resolved."""


class DetectionFailedError(HinLegacyError):
    """Raised when font detection cannot confidently identify a font."""