Scienco
=======
[![pipeline status][pipeline]](index.md)
[![coverage report][coverage]](index.md)
[![latest version][version]][pypi]
[![python requires][pyversions]][pypi]

Calculate the readability of text using one of a variety of computed indexes including:

- [Flesch-Kincaid score](api_reference.md#flesch_reading_ease_score)
- [Automated readability index](api_reference.md#automated_readability_index)
- [Coleman-Liau index](api_reference.md#coleman_liau_index)

Requirements
------------
Python 3.8+

Installation
------------
```
$ pip install scienco
```

Usage
-----
```python
>>> import scienco
>>> metrics = scienco.compute_metrics("Lorem ipsum dolor sit amet ...")
>>> metrics
Metrics(sentences=32, words=250, letters=1329, syllables=489, is_russian=False)
>>> indexes = scienco.compute_indexes(sentences=32, words=250, letters=1329, syllables=489, is_russian=False)
>>> indexes
Indexes(flesch_reading_ease_score=33.43, automated_readability_index=7.51, coleman_liau_index=11.67)
```

Distribution
------------
This project is licensed under the terms of the [MIT License](distribution.md).

[pypi]: <https://pypi.org/project/scienco>
[pipeline]: <https://gitlab.com/amalchuk/scienco/badges/master/pipeline.svg?style=flat-square>
[coverage]: <https://gitlab.com/amalchuk/scienco/badges/master/coverage.svg?style=flat-square>
[version]: <https://img.shields.io/pypi/v/scienco?color=blue&style=flat-square>
[pyversions]: <https://img.shields.io/pypi/pyversions/scienco?color=blue&style=flat-square>
