"""
Heuristic scoring utilities for font detection.
"""

from collections import Counter
from dataclasses import dataclass

from hinlegacy.detector.patterns import FONT_PATTERNS


@dataclass
class FontScore:
    font_slug: str
    score: float
    strong_hits: int
    medium_hits: int
    total_chars: int


def _count_matching_chars(text: str, charset: set[str]) -> int:
    return sum(1 for ch in text if ch in charset)


def _normalized_score(strong_hits: int, medium_hits: int, total_chars: int) -> float:
    if total_chars == 0:
        return 0.0
    raw = (strong_hits * 2.0) + (medium_hits * 1.0)
    return raw / total_chars


def score_fonts(text: str) -> list[FontScore]:
    cleaned = text.strip()
    total_chars = len(cleaned)

    scores: list[FontScore] = []
    for font_slug, groups in FONT_PATTERNS.items():
        strong_hits = _count_matching_chars(cleaned, groups["strong"])
        medium_hits = _count_matching_chars(cleaned, groups["medium"])
        score = _normalized_score(strong_hits, medium_hits, total_chars)

        scores.append(
            FontScore(
                font_slug=font_slug,
                score=score,
                strong_hits=strong_hits,
                medium_hits=medium_hits,
                total_chars=total_chars,
            )
        )

    scores.sort(key=lambda item: item.score, reverse=True)
    return scores


def confidence_from_scores(scores: list[FontScore]) -> float:
    if not scores:
        return 0.0
    if len(scores) == 1:
        return min(scores[0].score, 1.0)

    best = scores[0].score
    second = scores[1].score

    if best <= 0:
        return 0.0

    margin = best - second
    confidence = min(best + margin, 1.0)
    return round(confidence, 4)