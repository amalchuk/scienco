# -*- coding: utf-8 -*-

from typing import List

from scienco.metrics.processing import compute_metrics
from scienco.metrics.processing import sentences
from scienco.metrics.processing import syllables
from scienco.metrics.processing import words
from scienco.types import Metrics

__all__: List[str] = ["compute_metrics", "sentences", "syllables", "words", "Metrics"]
