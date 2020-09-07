API Reference
=============

Module `scienco.indexes`
------------------------
### scienco.indexes.**flesch_reading_ease_score**

Calculate the Flesch-Kincaid score.

**Syntax:**
```
flesch_reading_ease_score(sentences: int, words: int, syllables: int, *, is_russian: bool = False)
```

**Usage:**

- **sentences** - number of the sentences
- **words** - number of the words
- **syllables** - number of the syllables
- **is_russian** - specify whether you are using Russian language (otherwise English will be used)

**Example:**
```pycon
>>> flesch_reading_ease_score(sentences=100, words=10000, syllables=2500, is_russian=True)
76.73
```

**Returns:** `float`

### scienco.indexes.**automated_readability_index**

Calculate the Automated readability index.

**Syntax:**
```
automated_readability_index(sentences: int, words: int, letters: int, *, is_russian: bool = False)
```

**Usage:**

- **sentences** - number of the sentences
- **words** - number of the words
- **letters** - number of the letters
- **is_russian** - specify whether you are using Russian language (otherwise English will be used)

**Returns:** `float`

**Example:**
```pycon
>>> automated_readability_index(sentences=100, words=10000, letters=30000, is_russian=True)
15.79
```

### scienco.indexes.**coleman_liau_index**

Calculate the Coleman-Liau index.

**Syntax:**
```
coleman_liau_index(sentences: int, words: int, letters: int, *, is_russian: bool = False)
```

**Usage:**

- **sentences** - number of the sentences
- **words** - number of the words
- **letters** - number of the letters
- **is_russian** - specify whether you are using Russian language (otherwise English will be used)

**Returns:** `float`

**Example:**
```pycon
>>> coleman_liau_index(sentences=100, words=10000, letters=30000, is_russian=False)
1.54
```

### scienco.indexes.**compute_indexes**

Calculate the readability indexes.

**Syntax:**
```
compute_indexes(sentences: int, words: int, letters: int, syllables: int, *, is_russian: bool = False)
```

**Usage:**

- **sentences** - number of the sentences
- **words** - number of the words
- **letters** - number of the letters
- **syllables** - number of the syllables
- **is_russian** - specify whether you are using Russian language (otherwise English will be used)

**Returns:** [`Indexes`](#sciencotypesindexes)

**Example:**
```pycon
>>> compute_indexes(sentences=100, words=10000, letters=30000, syllables=2500, is_russian=False)
Indexes(flesch_reading_ease_score=84.19, automated_readability_index=42.7, coleman_liau_index=1.54)
```

Module `scienco.metrics`
------------------------
### scienco.metrics.**sentences**

Tokenize a paragraph into sentences.

**Syntax:**
```
sentences(string: str)
```

**Usage:**

- **string** - document text

**Returns:** [`Iterator[str]`][iterator]

### scienco.metrics.**words**

Tokenize a sentence into words.

**Syntax:**
```
words(string: str)
```

**Usage:**

- **string** - document text

**Returns:** [`Iterator[str]`][iterator]

### scienco.metrics.**syllables**

Return the number of syllables in a word.

**Syntax:**
```
syllables(string: str)
```

**Usage:**

- **string** - document text

**Returns:** `int`

### scienco.metrics.**compute_metrics**

Calculate the metrics.

**Syntax:**
```
compute_metrics(string: str)
```

**Usage:**

- **string** - document text

**Returns:** [`Metrics`](#sciencotypesmetrics)

Module `scienco.types`
----------------------
### scienco.types.**Metrics**

The [`namedtuple`][namedtuple] object with specified fields.

**Syntax:**
```python
class Metrics(NamedTuple):
    is_russian: bool
    sentences: int
    words: int
    letters: int
    syllables: int
```

### scienco.types.**Indexes**

The [`namedtuple`][namedtuple] object with specified fields.

**Syntax:**
```python
class Indexes(NamedTuple):
    flesch_reading_ease_score: float
    automated_readability_index: float
    coleman_liau_index: float
```

[iterator]: <https://docs.python.org/3/library/typing.html#typing.Iterator>
[namedtuple]: <https://docs.python.org/3/library/collections.html#collections.namedtuple>
