# -*- coding: utf-8 -*-

from itertools import chain
from typing import Iterator, List

__all__: List[str] = ["cyrillic_letters", "cyrillic_lowercase", "cyrillic_uppercase", "sentences_pattern", "words_pattern"]

sentences_pattern = "\x28\x5B\x2E\x3F\x21\u2026\x5D\x29\x5C\x73\x2B"
words_pattern = "\x28\x5B\x5E\x5C\x57\x5C\x64\x5D\x2B\x7C\x5C\x64\x2B\x7C\x5B\x5E\x5C\x77\x5C\x73\x5D\x29"

cyrillic_lowercase = "".join(map(chr, chain(range(1072, 1078), [1105], range(1078, 1104))))
cyrillic_uppercase = "".join(map(chr, chain(range(1040, 1046), [1025], range(1046, 1072))))
cyrillic_letters = cyrillic_lowercase + cyrillic_uppercase
