# -*- coding: utf-8 -*-

from scienco.utils import clamp

__all__ = ("automated_readability_index", "coleman_liau_index", "flesch_reading_ease_score")


def flesch_reading_ease_score(sentences: int, words: int, syllables: int) -> float:
    if not sentences or not words:
        return 0.0

    value = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return clamp(value, 0.0, 100.0)


def automated_readability_index(sentences: int, words: int, letters: int) -> float:
    if not sentences or not words:
        return 0.0

    value = 4.71 * (letters / words) + 0.5 * (words / sentences) - 21.43
    return max(0.0, value)


def coleman_liau_index(sentences: int, words: int, letters: int) -> float:
    if not words or words < 100:
        return 0.0

    value = 0.0588 * (letters / words * 100.0) - 0.296 * (sentences / words * 100.0) - 15.8
    return max(0.0, value)
