# -*- coding: utf-8 -*-

from itertools import chain
from typing import Final, Tuple

__all__: Final[Tuple[str, ...]] = (
    "cyrillic_letters",
    "cyrillic_lowercase",
    "cyrillic_uppercase",
    "english_vowels",
    "russian_vowels",
    "sentences_pattern",
    "words_pattern"
)

sentences_pattern: Final[str] = "\x28\x5B\x2E\x3F\x21\u2026\x5D\x29\x5C\x73\x2B"
words_pattern: Final[str] = "\x28\x5B\x5E\x5C\x57\x5C\x64\x5D\x2B\x7C\x5C\x64\x2B\x7C\x5B\x5E\x5C\x77\x5C\x73\x5D\x29"

cyrillic_lowercase: Final[str] = "".join(map(chr, chain(range(1072, 1078), [1105], range(1078, 1104))))
cyrillic_uppercase: Final[str] = "".join(map(chr, chain(range(1040, 1046), [1025], range(1046, 1072))))
cyrillic_letters: Final[str] = cyrillic_lowercase + cyrillic_uppercase

russian_vowels: Final[str] = "\u0430\u0435\u0451\u0438\u043E\u0443\u044B\u044D\u044E\u044F"
english_vowels: Final[str] = "\x61\x65\x69\x6F\x75\x79"
