Scienco
=======
[![pipeline status][pipeline]][homepage]
[![coverage report][coverage]][homepage]

Calculate the readability of text using one of a variety of computed indexes.

Installation
------------
```shell
$ make install
```

Usage
-----
```python
import scienco

string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel nunc
volutpat, consectetur risus ac, commodo est. Quisque eget diam ut nunc
finibus sodales vel blandit nibh. In placerat tempor sapien eget tincidunt.
Nullam risus purus, ullamcorper eget bibendum sed, interdum sit amet purus.
Aliquam congue elementum orci, id rhoncus orci varius sed. Donec auctor, ante
sit amet pretium gravida, nisl nisi vestibulum massa, id gravida leo lacus sed
mi. Sed ac consequat arcu, ut dictum justo. Proin at eros in tortor sagittis
volutpat id eget mauris. Duis ut consequat leo. Fusce molestie sit amet odio
ut vulputate.

Quisque at faucibus metus, quis mattis velit. Morbi nisl elit, pharetra vitae
velit ut, sodales molestie felis. Suspendisse cursus in nulla consectetur
porta. Nullam a massa dui. Donec tortor mi, iaculis vel sapien sed, sodales
vestibulum est. Vivamus finibus justo ut dolor egestas porttitor. Nulla nec
suscipit purus. Duis pretium ex orci. Nunc cursus enim nec est euismod
bibendum.

Phasellus lacus erat, dictum a malesuada dignissim, blandit in tellus. Quisque
vehicula nunc nulla, eget sollicitudin ligula feugiat vel. Morbi vitae libero
at est pellentesque sodales eget eu risus. Nam imperdiet tincidunt mattis.
Nullam a arcu risus. Etiam diam augue, rutrum convallis magna et, convallis
efficitur urna. Donec aliquam erat ex, eu convallis massa ultrices nec.
Curabitur eget sem venenatis, ornare tellus placerat, aliquet leo. Nam blandit
nisi ac pretium varius. Suspendisse eget nisl non nibh tristique cursus
feugiat id quam. Phasellus pretium mi nec mauris auctor, in placerat diam
cursus. Curabitur eleifend.
"""

scienco.compute_metrics(string)
# >>> Metrics(is_russian=False, sentences=32, words=250, letters=1329, syllables=489)

scienco.compute_indexes(sentences=32, words=250, letters=1329, syllables=489, is_russian=False)
# >>> Indexes(flesch_reading_ease_score=33.43, automated_readability_index=7.51, coleman_liau_index=11.67)
```

Distribution
------------
This project is licensed under the terms of the [MIT License](LICENSE).

[homepage]: <https://gitlab.com/amalchuk/scienco>
[pipeline]: <https://gitlab.com/amalchuk/scienco/badges/master/pipeline.svg?style=flat-square>
[coverage]: <https://gitlab.com/amalchuk/scienco/badges/master/coverage.svg?style=flat-square>
