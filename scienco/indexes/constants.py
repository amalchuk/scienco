# -*- coding: utf-8 -*-

from typing import List

from scienco.types import FloatEnum

__all__: List[str] = ["ARI_EN", "ARI_RU", "CLI_EN", "CLI_RU", "FRES_EN", "FRES_RU"]


class FRES_EN(FloatEnum):
    """
    Flesch-Kincaid score constants for english language.
    """
    X_GRADE = 206.835
    Y_GRADE = 1.015
    Z_GRADE = 84.6


class FRES_RU(FloatEnum):
    """
    Flesch-Kincaid score constants for russian language.
    """
    X_GRADE = 220.755
    Y_GRADE = 1.315
    Z_GRADE = 50.1


class ARI_EN(FloatEnum):
    """
    Automated readability index constants for english language.
    """
    X_GRADE = 4.71
    Y_GRADE = 0.5
    Z_GRADE = 21.43


class ARI_RU(FloatEnum):
    """
    Automated readability index constants for russian language.
    """
    X_GRADE = 6.26
    Y_GRADE = 0.2805
    Z_GRADE = 31.04


class CLI_EN(FloatEnum):
    """
    Coleman-Liau index constants for english language.
    """
    X_GRADE = 0.0588
    Y_GRADE = 0.296
    Z_GRADE = 15.8


class CLI_RU(FloatEnum):
    """
    Coleman-Liau index constants for russian language.
    """
    X_GRADE = 0.055
    Y_GRADE = 0.35
    Z_GRADE = 20.33
