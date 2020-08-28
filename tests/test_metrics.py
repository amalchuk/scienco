# -*- coding: utf-8 -*-

from scienco.metrics import compute_metrics, sentences, syllables, words


def test_sentences() -> None:
    string = "Я собираюсь сделать ему предложение, от которого он не сможет отказаться"
    sentences_list = tuple(sentences(string))
    assert len(sentences_list) == 1
    assert sentences_list[0] == string

    string = "I love the smell of napalm in the morning"
    sentences_list = tuple(sentences(string))
    assert len(sentences_list) == 1
    assert sentences_list[0] == string

    string = "Привет. Это я. Просто хотела узнать, не хотел бы ты встретиться спустя все эти годы."
    sentences_list = tuple(sentences(string))
    assert len(sentences_list) == 3
    assert sentences_list[0] == "Привет."
    assert sentences_list[1] == "Это я."
    assert sentences_list[2] == "Просто хотела узнать, не хотел бы ты встретиться спустя все эти годы."

    string = "Hello. It's me. I was wondering if after all these years you'd like to meet."
    sentences_list = tuple(sentences(string))
    assert len(sentences_list) == 3
    assert sentences_list[0] == "Hello."
    assert sentences_list[1] == "It's me."
    assert sentences_list[2] == "I was wondering if after all these years you'd like to meet."


def test_words() -> None:
    string = "Привет. Это я. Просто хотела узнать, не хотел бы ты встретиться спустя все эти годы."
    words_list = tuple(words(string))
    assert len(words_list) == 15

    string = "Hello. It's me. I was wondering if after all these years you'd like to meet."
    words_list = tuple(words(string))
    assert len(words_list) == 17


def test_syllables() -> None:
    words_list = ("мост", "война", "зеркальный", "масленица", "электричество", "стихотворение")
    for count, string in enumerate(words_list, start=1):
        assert syllables(string) == count

    words_list = ("bounce", "release", "absolute", "entertainment", "understandable", "availability")
    for count, string in enumerate(words_list, start=1):
        assert syllables(string) == count


def test_compute_metrics() -> None:
    string = "Привет. Это я. Просто хотела узнать, не хотел бы ты встретиться спустя все эти годы."
    metrics = compute_metrics(string)
    assert metrics == {"is_russian": True, "sentences": 3, "words": 15, "letters": 66, "syllables": 27}

    string = "Hello. It's me. I was wondering if after all these years you'd like to meet."
    metrics = compute_metrics(string)
    assert metrics == {"is_russian": False, "sentences": 3, "words": 17, "letters": 57, "syllables": 21}
