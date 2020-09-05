Scienco
=======
[![pipeline status][pipeline]][homepage]
[![coverage report][coverage]][homepage]

Calculate the readability of text using one of a variety of computed indexes.

Requirements
------------
Python 3.6+

Installation
------------
```shell
$ make install
```

Usage
-----
```python
>>> import scienco

# Calculate the metrics:
>>> scienco.compute_metrics("Lorem ipsum dolor sit amet ...")
Metrics(is_russian=False, sentences=32, words=250, letters=1329, syllables=489)

# Calculate the readability indexes:
>>> scienco.compute_indexes(sentences=32, words=250, letters=1329, syllables=489, is_russian=False)
Indexes(flesch_reading_ease_score=33.43, automated_readability_index=7.51, coleman_liau_index=11.67)
```

Distribution
------------
This project is licensed under the terms of the [MIT License](LICENSE).

[homepage]: <https://gitlab.com/amalchuk/scienco>
[pipeline]: <https://gitlab.com/amalchuk/scienco/badges/master/pipeline.svg?style=flat-square>
[coverage]: <https://gitlab.com/amalchuk/scienco/badges/master/coverage.svg?style=flat-square>
