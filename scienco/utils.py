# -*- coding: utf-8 -*-

from typing import TypeVar

__all__ = ("clamp",)

C = TypeVar("C", float, str, bytes)


def clamp(value: C, min_value: C, max_value: C) -> C:
    """
    Limits a provided value between two specified bounds.
    """
    return max(min_value, min(value, max_value))
