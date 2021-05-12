# -*- coding: utf-8 -*-

from typing import Final, Tuple

from scienco.indexes.constants import ARI_EN
from scienco.indexes.constants import ARI_RU
from scienco.indexes.constants import CLI_EN
from scienco.indexes.constants import CLI_RU
from scienco.indexes.constants import FRES_EN
from scienco.indexes.constants import FRES_RU
from scienco.types import Indexes
from scienco.utils import clamp

__all__: Final[Tuple[str, ...]] = (
    "automated_readability_index", "coleman_liau_index", "compute_indexes", "flesch_reading_ease_score", "Indexes"
)


def flesch_reading_ease_score(sentences: int, words: int, syllables: int, *, is_russian: bool = False) -> float:
    """
    Calculate the Flesch-Kincaid score.
    """
    if not sentences or not words:
        return 0.0

    # Flesch-Kincaid score constants:
    x_grade: float = FRES_RU.X_GRADE if is_russian else FRES_EN.X_GRADE
    y_grade: float = FRES_RU.Y_GRADE if is_russian else FRES_EN.Y_GRADE
    z_grade: float = FRES_RU.Z_GRADE if is_russian else FRES_EN.Z_GRADE

    value: float = x_grade - y_grade * (words / sentences) - z_grade * (syllables / words)
    return clamp(value, 0.0, 100.0)


def automated_readability_index(sentences: int, words: int, letters: int, *, is_russian: bool = False) -> float:
    """
    Calculate the Automated readability index.
    """
    if not sentences or not words:
        return 0.0

    # Automated readability index constants:
    x_grade: float = ARI_RU.X_GRADE if is_russian else ARI_EN.X_GRADE
    y_grade: float = ARI_RU.Y_GRADE if is_russian else ARI_EN.Y_GRADE
    z_grade: float = ARI_RU.Z_GRADE if is_russian else ARI_EN.Z_GRADE

    value: float = x_grade * (letters / words) + y_grade * (words / sentences) - z_grade
    return max(0.0, value)


def coleman_liau_index(sentences: int, words: int, letters: int, *, is_russian: bool = False) -> float:
    """
    Calculate the Coleman-Liau index.
    """
    if not words or words < 100:
        return 0.0

    # Coleman-Liau index constants:
    x_grade: float = CLI_RU.X_GRADE if is_russian else CLI_EN.X_GRADE
    y_grade: float = CLI_RU.Y_GRADE if is_russian else CLI_EN.Y_GRADE
    z_grade: float = CLI_RU.Z_GRADE if is_russian else CLI_EN.Z_GRADE

    value: float = x_grade * (letters / words * 100.0) - y_grade * (sentences / words * 100.0) - z_grade
    return max(0.0, value)


def compute_indexes(sentences: int, words: int, letters: int, syllables: int, *, is_russian: bool = False) -> Indexes:
    """
    Calculate the readability indexes.
    """
    flesch_reading_ease_score_value: float = flesch_reading_ease_score(sentences, words, syllables, is_russian=is_russian)
    automated_readability_index_value: float = automated_readability_index(sentences, words, letters, is_russian=is_russian)
    coleman_liau_index_value: float = coleman_liau_index(sentences, words, letters, is_russian=is_russian)
    return Indexes(
        flesch_reading_ease_score=flesch_reading_ease_score_value,
        automated_readability_index=automated_readability_index_value,
        coleman_liau_index=coleman_liau_index_value)
