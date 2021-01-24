# -*- coding: utf-8 -*-

from itertools import chain
from itertools import product
import re
from string import ascii_letters
from typing import Iterator, List

from scienco.metrics.constants import cyrillic_letters
from scienco.metrics.constants import sentences_pattern as _sentences_pattern
from scienco.metrics.constants import words_pattern as _words_pattern
from scienco.types import Metrics

__all__: List[str] = ["compute_metrics", "sentences", "syllables", "words", "Metrics"]

sentences_pattern = re.compile(_sentences_pattern, re.UNICODE)
words_pattern = re.compile(_words_pattern, re.UNICODE)


def sentences(string: str) -> Iterator[str]:
    """
    Tokenize a paragraph into sentences.
    """
    previous = 0

    for match in sentences_pattern.finditer(string):
        delimiter = match.group(1)
        start = match.start()

        yield string[previous:start] + delimiter
        previous = match.end()

    if previous < len(string):
        yield string[previous:]


def words(string: str) -> Iterator[str]:
    """
    Tokenize a sentence into words.
    """
    for match in words_pattern.finditer(string):
        word = match.group(1)

        if word.isalnum():
            yield word


def syllables(string: str) -> int:
    """
    Return the number of syllables in a word.
    """
    string = string.lower() if not string.islower() else string

    # Russian vowels:
    vowels = "\u0430\u0435\u0451\u0438\u043E\u0443\u044B\u044D\u044E\u044F"

    if any(vowel in string for vowel in vowels):
        return sum(map(string.count, vowels))

    # English vowels:
    vowels = "\x61\x65\x69\x6F\x75\x79"
    count = 0

    if any(vowel in string for vowel in vowels):
        count = sum(map(string.count, vowels))
        count = count - string.endswith("\x65")

        diphthongs: Iterator[str] = map("".join, product(vowels, repeat=2))
        count = count - sum(map(string.count, diphthongs))

        triphthongs: Iterator[str] = map("".join, product(vowels, repeat=3))
        count = count - sum(map(string.count, triphthongs))

        if string.endswith("\x6C\x65") or string.endswith("\x6C\x65\x73"):
            string, _ = string.split("\x6C\x65", 1)
            count = count + all(not string.endswith(vowel) for vowel in vowels)

    return max(1, count)


def compute_metrics(string: str) -> Metrics:
    """
    Calculate the metrics.
    """
    russian_letters = sum(map(string.count, cyrillic_letters))
    english_letters = sum(map(string.count, ascii_letters))

    is_russian = russian_letters > english_letters
    del english_letters, russian_letters

    sentences_list = list(sentences(string))
    sentences_count = len(sentences_list)

    words_list = list(chain.from_iterable(map(words, sentences_list)))
    words_count = len(words_list)
    del sentences_list

    letters_count = sum(map(len, words_list))
    syllables_count = sum(map(syllables, words_list))
    del words_list

    return Metrics(
        sentences=sentences_count,
        words=words_count,
        letters=letters_count,
        syllables=syllables_count,
        is_russian=is_russian)
