Scienco
=======
[![pipeline status][pipeline]][homepage]
[![coverage report][coverage]][homepage]
[![distribution][license]](LICENSE)

Calculate the readability of text using one of a variety of computed indexes including:

- Flesch-Kincaid score
- Automated readability index
- Coleman-Liau index

Requirements
------------
Python 3.6+

Installation
------------
```
$ pip install scienco
```

Usage
-----
```pycon
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
This project is licensed under the terms of the [MIT License](LICENSE).

Links
-----
- Documentation: <https://scienco.readable.pw>
- Code: <https://gitlab.com/amalchuk/scienco>
- GitHub mirror: <https://github.com/amalchuk/scienco>

[homepage]: <https://gitlab.com/amalchuk/scienco>
[pipeline]: <https://gitlab.com/amalchuk/scienco/badges/master/pipeline.svg?style=flat-square>
[coverage]: <https://gitlab.com/amalchuk/scienco/badges/master/coverage.svg?style=flat-square>
[license]: <https://img.shields.io/github/license/amalchuk/scienco?color=blue&style=flat-square>
