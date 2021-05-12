# -*- coding: utf-8 -*-

from typing import Final, Tuple

from scienco.types import FloatEnum

__all__: Final[Tuple[str, ...]] = ("ARI_EN", "ARI_RU", "CLI_EN", "CLI_RU", "FRES_EN", "FRES_RU")


class FRES_EN(FloatEnum):
    """
    Flesch-Kincaid score constants for english language.
    """
    X_GRADE: Final[float] = 206.835
    Y_GRADE: Final[float] = 1.015
    Z_GRADE: Final[float] = 84.6


class FRES_RU(FloatEnum):
    """
    Flesch-Kincaid score constants for russian language.
    """
    X_GRADE: Final[float] = 220.755
    Y_GRADE: Final[float] = 1.315
    Z_GRADE: Final[float] = 50.1


class ARI_EN(FloatEnum):
    """
    Automated readability index constants for english language.
    """
    X_GRADE: Final[float] = 4.71
    Y_GRADE: Final[float] = 0.5
    Z_GRADE: Final[float] = 21.43


class ARI_RU(FloatEnum):
    """
    Automated readability index constants for russian language.
    """
    X_GRADE: Final[float] = 6.26
    Y_GRADE: Final[float] = 0.2805
    Z_GRADE: Final[float] = 31.04


class CLI_EN(FloatEnum):
    """
    Coleman-Liau index constants for english language.
    """
    X_GRADE: Final[float] = 0.0588
    Y_GRADE: Final[float] = 0.296
    Z_GRADE: Final[float] = 15.8


class CLI_RU(FloatEnum):
    """
    Coleman-Liau index constants for russian language.
    """
    X_GRADE: Final[float] = 0.055
    Y_GRADE: Final[float] = 0.35
    Z_GRADE: Final[float] = 20.33
