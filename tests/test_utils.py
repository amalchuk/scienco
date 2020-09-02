# -*- coding: utf-8 -*-

from scienco.utils import clamp


def test_clamp() -> None:
    assert clamp(0.0, 1.0, 2.0) == 1.0
    assert clamp(1.0, 1.0, 2.0) == 1.0
    assert clamp(2.0, 1.0, 2.0) == 2.0
    assert clamp(3.0, 1.0, 2.0) == 2.0

    assert clamp("a", "b", "c") == "b"
    assert clamp("b", "b", "c") == "b"
    assert clamp("c", "b", "c") == "c"
    assert clamp("d", "b", "c") == "c"

    assert clamp(b"a", b"b", b"c") == b"b"
    assert clamp(b"b", b"b", b"c") == b"b"
    assert clamp(b"c", b"b", b"c") == b"c"
    assert clamp(b"d", b"b", b"c") == b"c"
