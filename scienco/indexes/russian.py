# -*- coding: utf-8 -*-

from scienco.utils import clamp

__all__ = ("automated_readability_index", "coleman_liau_index", "flesch_reading_ease_score")


def flesch_reading_ease_score(sentences: int, words: int, syllables: int) -> float:
    if not sentences or not words:
        return 0.0

    value = 220.755 - 1.315 * (words / sentences) - 50.1 * (syllables / words)
    return clamp(value, 0.0, 100.0)


def automated_readability_index(sentences: int, words: int, letters: int) -> float:
    if not sentences or not words:
        return 0.0

    value = 6.26 * (letters / words) + 0.2805 * (words / sentences) - 31.04
    return max(0.0, value)


def coleman_liau_index(sentences: int, words: int, letters: int) -> float:
    if not words or words < 100:
        return 0.0

    value = 0.055 * (letters / words * 100.0) - 0.35 * (sentences / words * 100.0) - 20.33
    return max(0.0, value)
