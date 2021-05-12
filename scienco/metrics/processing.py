# -*- coding: utf-8 -*-

from itertools import chain
from itertools import product
import re
from string import ascii_letters
from typing import Final, Iterator, Pattern, Tuple

from scienco.metrics.constants import cyrillic_letters
from scienco.metrics.constants import english_vowels
from scienco.metrics.constants import russian_vowels
from scienco.metrics.constants import sentences_pattern as _sentences_pattern
from scienco.metrics.constants import words_pattern as _words_pattern
from scienco.types import Metrics

__all__: Final[Tuple[str, ...]] = ("compute_metrics", "sentences", "syllables", "words", "Metrics")

sentences_pattern: Final[Pattern[str]] = re.compile(_sentences_pattern, re.UNICODE)
words_pattern: Final[Pattern[str]] = re.compile(_words_pattern, re.UNICODE)


def sentences(string: str, /) -> Iterator[str]:
    """
    Tokenize a paragraph into sentences.
    """
    delimiter: str
    start: int
    previous: int = 0

    for match in sentences_pattern.finditer(string):
        delimiter = match.group(1)
        start = match.start()

        yield string[previous:start] + delimiter
        previous = match.end()

    if previous < len(string):
        yield string[previous:]


def words(string: str, /) -> Iterator[str]:
    """
    Tokenize a sentence into words.
    """
    word: str

    for match in words_pattern.finditer(string):
        word = match.group(1)

        if word.isalnum():
            yield word


def syllables(string: str, /) -> int:
    """
    Return the number of syllables in a word.
    """
    string = string.lower() if not string.islower() else string

    if any(vowel in string for vowel in russian_vowels):
        return sum(map(string.count, russian_vowels))

    count: int = 0

    if any(vowel in string for vowel in english_vowels):
        count = sum(map(string.count, english_vowels))
        count = count - string.endswith("\x65")

        diphthongs: Iterator[str] = map("".join, product(english_vowels, repeat=2))
        count = count - sum(map(string.count, diphthongs))

        triphthongs: Iterator[str] = map("".join, product(english_vowels, repeat=3))
        count = count - sum(map(string.count, triphthongs))

        if string.endswith("\x6C\x65") or string.endswith("\x6C\x65\x73"):
            string, _ = string.split("\x6C\x65", 1)
            count = count + all(not string.endswith(vowel) for vowel in english_vowels)

    return max(1, count)


def compute_metrics(string: str, /) -> Metrics:
    """
    Calculate the metrics.
    """
    russian_letters: int = sum(map(string.count, cyrillic_letters))
    english_letters: int = sum(map(string.count, ascii_letters))

    is_russian: bool = russian_letters > english_letters
    del english_letters, russian_letters

    sentences_list: Tuple[str, ...] = tuple(sentences(string))
    sentences_count: int = len(sentences_list)

    words_list: Tuple[str, ...] = tuple(chain.from_iterable(map(words, sentences_list)))
    words_count: int = len(words_list)
    del sentences_list

    letters_count: int = sum(map(len, words_list))
    syllables_count: int = sum(map(syllables, words_list))
    del words_list

    return Metrics(
        sentences=sentences_count,
        words=words_count,
        letters=letters_count,
        syllables=syllables_count,
        is_russian=is_russian)
