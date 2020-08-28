# -*- coding: utf-8 -*-

from typing import Any, Protocol, TypeVar, runtime_checkable

__all__ = ("clamp",)

C = TypeVar("C", bound="Comparable")


@runtime_checkable
class Comparable(Protocol):  # pragma: no cover
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...


def clamp(value: C, min_value: C, max_value: C) -> C:
    """
    Limits a provided value between two specified bounds.
    """
    return max(min_value, min(value, max_value))
