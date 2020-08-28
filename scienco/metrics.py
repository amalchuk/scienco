# -*- coding: utf-8 -*-

import re
from itertools import chain, product
from string import ascii_letters
from typing import Iterator, TypedDict

from scienco.constants import cyrillic_letters, sentences_pattern, words_pattern

__all__ = ("compute_metrics", "sentences", "syllables", "words")


class Metrics(TypedDict):
    is_russian: bool
    sentences: int
    words: int
    letters: int
    syllables: int


def sentences(string: str) -> Iterator[str]:
    pattern = re.compile(sentences_pattern, re.UNICODE)
    previous = 0

    for match in pattern.finditer(string):
        delimiter = match.group(1)
        start = match.start()

        yield string[previous:start] + delimiter
        previous = match.end()

    if previous < len(string):
        yield string[previous:]


def words(string: str) -> Iterator[str]:
    pattern = re.compile(words_pattern, re.UNICODE)

    for match in pattern.finditer(string):
        word = match.group(1)

        if word.isalnum():
            yield word


def syllables(string: str) -> int:
    string = string.lower() if not string.islower() else string

    # Russian vowels:
    vowels = "\u0430\u0435\u0451\u0438\u043E\u0443\u044B\u044D\u044E\u044F"

    if any(vowel in string for vowel in vowels):
        return sum(map(string.count, vowels))

    # English vowels:
    vowels = "\x61\x65\x69\x6F\x75\x79"
    count = 0

    if any(vowel in string for vowel in vowels):
        count += sum(map(string.count, vowels))
        count -= string.endswith("\x65")

        diphthongs: Iterator[str] = map("".join, product(vowels, repeat=2))
        count -= sum(map(string.count, diphthongs))

        triphthongs: Iterator[str] = map("".join, product(vowels, repeat=3))
        count -= sum(map(string.count, triphthongs))

        if string.endswith("\x6C\x65") or string.endswith("\x6C\x65\x73"):
            string, _ = string.split("\x6C\x65", 1)
            count += all(not string.endswith(vowel) for vowel in vowels)

    return count or 1


def compute_metrics(string: str) -> Metrics:
    russian_letters = sum(map(string.count, cyrillic_letters))
    english_letters = sum(map(string.count, ascii_letters))

    is_russian = russian_letters > english_letters
    del english_letters, russian_letters

    sentences_list = tuple(sentences(string))
    sentences_count = len(sentences_list)

    words_list = tuple(chain.from_iterable(map(words, sentences_list)))
    words_count = len(words_list)
    del sentences_list

    letters_count = sum(map(len, words_list))
    syllables_count = sum(map(syllables, words_list))
    del words_list

    return {
        "is_russian": is_russian,
        "sentences": sentences_count,
        "words": words_count,
        "letters": letters_count,
        "syllables": syllables_count
    }
