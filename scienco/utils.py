# -*- coding: utf-8 -*-

from typing import List, TypeVar

__all__: List[str] = ["clamp"]

_C = TypeVar("_C", float, str, bytes)


def clamp(value: _C, min_value: _C, max_value: _C) -> _C:
    """
    Limits a provided value between two specified bounds.
    """
    return max(min_value, min(value, max_value))
