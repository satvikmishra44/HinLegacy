"""
Shared data models used across HinLegacy.
"""

from dataclasses import dataclass

@dataclass
class DetectionResult:
    font_slug: str
    confidence: float
    method: str

@dataclass
class ConversionResult:
    unicode_text: str
    detected_font: str
    confidence: float
    detection_method: str