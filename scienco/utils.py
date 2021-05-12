# -*- coding: utf-8 -*-

from typing import Final, Tuple, TypeVar

__all__: Final[Tuple[str, ...]] = ("clamp",)

_C = TypeVar("_C", float, str, bytes)


def clamp(value: _C, min_value: _C, max_value: _C, /) -> _C:
    """
    Limits a provided value between two specified bounds.

    Example:
    >>> clamp(1.0, 2.0, 3.0)
    2.0
    >>> clamp(4.0, 2.0, 3.0)
    3.0
    """
    return max(min_value, min(value, max_value))
