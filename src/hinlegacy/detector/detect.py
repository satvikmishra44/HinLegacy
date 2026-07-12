"""
Font detection logic.
"""

from __future__ import annotations

from hinlegacy.detector.heuristics import confidence_from_scores, score_fonts
from hinlegacy.exceptions import DetectionFailedError
from hinlegacy.models import DetectionResult

MIN_DETECTABLE_LENGTH = 2
MIN_CONFIDENCE = 0.20


def detect_font(text: str) -> DetectionResult:
    cleaned = text.strip()

    if not cleaned:
        raise DetectionFailedError("Cannot detect font from empty text.")

    if len(cleaned) < MIN_DETECTABLE_LENGTH:
        raise DetectionFailedError(
            f"Input text is too short for reliable detection. Minimum length: {MIN_DETECTABLE_LENGTH}."
        )

    scores = score_fonts(cleaned)
    best = scores[0]
    confidence = confidence_from_scores(scores)

    if best.score <= 0:
        raise DetectionFailedError("Could not detect font: no pattern evidence found.")

    if confidence < MIN_CONFIDENCE:
        raise DetectionFailedError(
            f"Detection confidence too low: {confidence:.2f}. Best candidate was {best.font_slug}."
        )

    return DetectionResult(
        font_slug=best.font_slug,
        confidence=confidence,
        method="heuristic_token_pattern",
    )