# -*- coding: utf-8 -*-

from scienco.indexes import automated_readability_index, coleman_liau_index, compute_indexes, flesch_reading_ease_score


def test_flesch_reading_ease_score() -> None:
    value = flesch_reading_ease_score(sentences=0, words=10000, syllables=2500, is_russian=True)
    assert value == 0.0

    value = flesch_reading_ease_score(sentences=100, words=0, syllables=2500, is_russian=True)
    assert value == 0.0

    value = flesch_reading_ease_score(sentences=0, words=10000, syllables=2500, is_russian=False)
    assert value == 0.0

    value = flesch_reading_ease_score(sentences=100, words=0, syllables=2500, is_russian=False)
    assert value == 0.0

    value = flesch_reading_ease_score(sentences=100, words=10000, syllables=2500, is_russian=True)
    assert 76.0 <= value <= 77.0

    value = flesch_reading_ease_score(sentences=100, words=10000, syllables=2500, is_russian=False)
    assert 84.0 <= value <= 85.0


def test_automated_readability_index() -> None:
    value = automated_readability_index(sentences=0, words=10000, letters=30000, is_russian=True)
    assert value == 0.0

    value = automated_readability_index(sentences=100, words=0, letters=30000, is_russian=True)
    assert value == 0.0

    value = automated_readability_index(sentences=0, words=10000, letters=30000, is_russian=False)
    assert value == 0.0

    value = automated_readability_index(sentences=100, words=0, letters=30000, is_russian=False)
    assert value == 0.0

    value = automated_readability_index(sentences=100, words=10000, letters=30000, is_russian=True)
    assert 15.0 <= value <= 16.0

    value = automated_readability_index(sentences=100, words=10000, letters=30000, is_russian=False)
    assert 42.0 <= value <= 43.0


def test_coleman_liau_index() -> None:
    value = coleman_liau_index(sentences=100, words=0, letters=30000, is_russian=True)
    assert value == 0.0

    value = coleman_liau_index(sentences=100, words=90, letters=30000, is_russian=True)
    assert value == 0.0

    value = coleman_liau_index(sentences=100, words=0, letters=30000, is_russian=False)
    assert value == 0.0

    value = coleman_liau_index(sentences=100, words=90, letters=30000, is_russian=False)
    assert value == 0.0

    value = coleman_liau_index(sentences=100, words=10000, letters=30000, is_russian=True)
    assert 0.0 <= value <= 1.0

    value = coleman_liau_index(sentences=100, words=10000, letters=30000, is_russian=False)
    assert 1.0 <= value <= 2.0


def test_compute_indexes() -> None:
    value = compute_indexes(sentences=100, words=10000, letters=30000, syllables=2500, is_russian=True)
    assert 76.0 <= value["flesch_reading_ease_score"] <= 77.0
    assert 15.0 <= value["automated_readability_index"] <= 16.0
    assert 0.0 <= value["coleman_liau_index"] <= 1.0

    value = compute_indexes(sentences=100, words=10000, letters=30000, syllables=2500, is_russian=False)
    assert 84.0 <= value["flesch_reading_ease_score"] <= 85.0
    assert 42.0 <= value["automated_readability_index"] <= 43.0
    assert 1.0 <= value["coleman_liau_index"] <= 2.0
