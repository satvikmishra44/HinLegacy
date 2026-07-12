"""
Font detection logic.
"""

from hinlegacy.detector.heuristics import confidence_from_scores, score_fonts
from hinlegacy.exceptions import DetectionFailedError
from hinlegacy.models import DetectionResult

MIN_DETECTABLE_LENGTH = 3
MIN_CONFIDENCE = 0.15


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

    if best.score <= 0 or confidence < MIN_CONFIDENCE:
        raise DetectionFailedError("Could not confidently detect the legacy font.")

    return DetectionResult(
        font_slug=best.font_slug,
        confidence=confidence,
        method="heuristic_char_pattern",
    )