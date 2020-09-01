# -*- coding: utf-8 -*-

"""
Calculate the readability of text using one of a variety of computed indexes.
"""

from scienco.indexes import automated_readability_index, coleman_liau_index, compute_indexes, flesch_reading_ease_score
from scienco.metrics import compute_metrics, sentences, syllables, words

__all__ = (
    "automated_readability_index", "coleman_liau_index", "compute_indexes", "flesch_reading_ease_score",
    "compute_metrics", "sentences", "syllables", "words"
)
