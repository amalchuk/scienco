# -*- coding: utf-8 -*-

from typing import TypedDict

from scienco.indexes import english, russian

__all__ = ("automated_readability_index", "coleman_liau_index", "compute_indexes", "flesch_reading_ease_score")


class Indexes(TypedDict):
    flesch_reading_ease_score: float
    automated_readability_index: float
    coleman_liau_index: float


def flesch_reading_ease_score(sentences: int, words: int, syllables: int, *, is_russian: bool = False) -> float:
    method = russian.flesch_reading_ease_score if is_russian else english.flesch_reading_ease_score
    return method(sentences, words, syllables)


def automated_readability_index(sentences: int, words: int, letters: int, *, is_russian: bool = False) -> float:
    method = russian.automated_readability_index if is_russian else english.automated_readability_index
    return method(sentences, words, letters)


def coleman_liau_index(sentences: int, words: int, letters: int, *, is_russian: bool = False) -> float:
    method = russian.coleman_liau_index if is_russian else english.coleman_liau_index
    return method(sentences, words, letters)


def compute_indexes(sentences: int, words: int, letters: int, syllables: int, *, is_russian: bool = False) -> Indexes:
    return {
        "flesch_reading_ease_score": flesch_reading_ease_score(sentences, words, syllables, is_russian=is_russian),
        "automated_readability_index": automated_readability_index(sentences, words, letters, is_russian=is_russian),
        "coleman_liau_index": coleman_liau_index(sentences, words, letters, is_russian=is_russian)
    }
