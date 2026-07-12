"""
Heuristic scoring utilities for font detection.
"""

from __future__ import annotations

from dataclasses import dataclass

from hinlegacy.detector.patterns import FONT_PATTERNS, FONT_UNIQUE_TOKENS


@dataclass(frozen=True)
class FontScore:
    font_slug: str
    score: float
    strong_hits: int
    medium_hits: int
    unique_hits: int
    text_length: int


def _count_token_occurrences(text: str, token: str) -> int:
    if not token:
        return 0
    return text.count(token)


def _score_font(text: str, font_slug: str) -> FontScore:
    pattern_group = FONT_PATTERNS[font_slug]
    strong_tokens = pattern_group["strong_tokens"]
    medium_tokens = pattern_group["medium_tokens"]
    unique_tokens = FONT_UNIQUE_TOKENS.get(font_slug, ())

    strong_hits = sum(_count_token_occurrences(text, token) for token in strong_tokens)
    medium_hits = sum(_count_token_occurrences(text, token) for token in medium_tokens)
    unique_hits = sum(_count_token_occurrences(text, token) for token in unique_tokens)

    raw_score = (strong_hits * 3.0) + (medium_hits * 1.0) + (unique_hits * 5.0)
    normalized = raw_score / max(len(text), 1)

    return FontScore(
        font_slug=font_slug,
        score=normalized,
        strong_hits=strong_hits,
        medium_hits=medium_hits,
        unique_hits=unique_hits,
        text_length=len(text),
    )


def score_fonts(text: str) -> list[FontScore]:
    scores = [_score_font(text, font_slug) for font_slug in FONT_PATTERNS]
    scores.sort(key=lambda item: item.score, reverse=True)
    return scores


def confidence_from_scores(scores: list[FontScore]) -> float:
    if not scores:
        return 0.0

    if len(scores) == 1:
        return round(min(scores[0].score, 1.0), 4)

    best = scores[0]
    second = scores[1]

    if best.score <= 0:
        return 0.0

    margin = best.score - second.score
    confidence = best.score + (margin * 2.0) + (best.unique_hits * 0.08)
    return round(min(confidence, 1.0), 4)