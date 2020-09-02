# -*- coding: utf-8 -*-

from enum import Enum
from typing import NamedTuple

__all__ = ("FloatEnum", "Indexes", "Metrics")


class FloatEnum(float, Enum):
    """
    Enum where members are also (and must be) floats.
    """


class Metrics(NamedTuple):
    is_russian: bool
    sentences: int
    words: int
    letters: int
    syllables: int


class Indexes(NamedTuple):
    flesch_reading_ease_score: float
    automated_readability_index: float
    coleman_liau_index: float
