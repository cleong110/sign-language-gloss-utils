from sign_language_gloss_utils.glosses.text_utils import (
    get_glosses_set_from_text,
    get_glosses_from_text,
    preprocess_text,
)


def test_preprocess():
    texts = [
        ("In the beginning God created the heavens and the earth.", 10),
        ("And God said, “Let there be light,” and there was light.", 11),
    ]
    for text, expected_len in texts:
        lemmas = preprocess_text(text)
        assert len(lemmas) == expected_len, f"lemmatization no work: {text}: {lemmas}"


def test_preprocess_remove_stopwords():
    texts = [
        ("In the beginning God created the heavens and the earth.", 5),
        ("And God said, “Let there be light,” and there was light.", 5),
    ]
    for text, expected_len in texts:
        lemmas = preprocess_text(text, remove_stopwords=True)
        assert len(lemmas) == expected_len, f"stopword remove no work: {text}: {lemmas}"


def test_get_glosses_list():
    # lifted from ASL Citizen manually
    test_values = [
        (
            "In the beginning God created the heavens and the earth.",
            ["IN", "THE", "BEGINNING", "GOD", "CREATE", "THE", "HEAVEN", "AND", "THE", "EARTH"],
            ["BEGINNING", "GOD", "CREATE", "HEAVEN", "EARTH"],
        ),
        (
            "And God said, “Let there be light,” and there was light.",
            ["AND", "GOD", "THERE", "LIGHT", "AND", "THERE", "LIGHT"],
            ["GOD", "LIGHT", "LIGHT"],
        ),
    ]

    for text, expected_list, expected_list_without_stopwords in test_values:
        retrieved_list = get_glosses_from_text(text, expected_list)

        assert retrieved_list == expected_list
        retrieved_list = get_glosses_from_text(text, expected_list, remove_stopwords=True)
        assert retrieved_list == expected_list_without_stopwords


def test_get_glosses_set():
    # lifted from ASL Citizen manually
    test_values = [
        (
            "In the beginning God created the heavens and the earth.",
            {"IN", "BEGINNING", "GOD", "CREATE", "HEAVEN", "EARTH", "THE", "AND"},
            {"BEGINNING", "GOD", "CREATE", "HEAVEN", "EARTH"},
        ),
        (
            "And God said, “Let there be light,” and there was light.",
            {"AND", "GOD", "LIGHT", "THERE"},
            {"GOD", "LIGHT"},
        ),
    ]

    for text, expected_set, expected_set_without_stopwords in test_values:
        retrieved_set = get_glosses_set_from_text(text, expected_set)

        assert retrieved_set == expected_set
        retrieved_set = get_glosses_set_from_text(text, expected_set, remove_stopwords=True)
        assert retrieved_set == expected_set_without_stopwords
