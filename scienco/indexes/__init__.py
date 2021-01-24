# -*- coding: utf-8 -*-

from typing import List

from scienco.indexes.processing import automated_readability_index
from scienco.indexes.processing import coleman_liau_index
from scienco.indexes.processing import compute_indexes
from scienco.indexes.processing import flesch_reading_ease_score
from scienco.types import Indexes

__all__: List[str] = [
    "automated_readability_index", "coleman_liau_index", "compute_indexes", "flesch_reading_ease_score", "Indexes"
]
