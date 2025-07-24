from sign_language_gloss_utils.glosses.text_utils import get_glosses_set_from_text, preprocess_text


def test_preprocess():
    texts = [
        ("In the beginning God created the heavens and the earth.", 10),
        ("And God said, “Let there be light,” and there was light.", 11),
    ]
    for text, expected_len in texts:
        lemmas = preprocess_text(text)
        assert len(lemmas) == expected_len, f"lemmatization no work: {text}: {lemmas}"


def test_get_glosses():
    # lifted from ASL Citizen manually
    pairs = [
        (
            "In the beginning God created the heavens and the earth.",
            {"IN", "BEGINNING", "GOD", "CREATE", "HEAVEN", "EARTH", "THE", "AND"},
        ),
        ("And God said, “Let there be light,” and there was light.", {"AND", "GOD", "LIGHT", "THERE"}),
    ]

    for text, expected_set in pairs:
        retrieved_set = get_glosses_set_from_text(text, expected_set)
        assert retrieved_set == expected_set
