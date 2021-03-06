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

    assert clamp(b"e", b"f", b"g") == b"f"
    assert clamp(b"f", b"f", b"g") == b"f"
    assert clamp(b"g", b"f", b"g") == b"g"
    assert clamp(b"h", b"f", b"g") == b"g"
