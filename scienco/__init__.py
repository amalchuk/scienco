# -*- coding: utf-8 -*-

"""
Calculate the readability of text using one of a variety of computed indexes.
"""

from typing import List

from scienco.indexes import automated_readability_index
from scienco.indexes import coleman_liau_index
from scienco.indexes import compute_indexes
from scienco.indexes import flesch_reading_ease_score
from scienco.metrics import compute_metrics
from scienco.metrics import sentences
from scienco.metrics import syllables
from scienco.metrics import words
from scienco.types import Indexes
from scienco.types import Metrics

__all__: List[str] = [
    "automated_readability_index", "coleman_liau_index", "compute_indexes", "flesch_reading_ease_score",
    "compute_metrics", "sentences", "syllables", "words",
    "Indexes", "Metrics"
]
