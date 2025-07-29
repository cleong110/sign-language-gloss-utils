import spacy


def preprocess_text(
    text,
    spacy_pipeline: str | spacy.Language = "en_core_web_sm",
    uppercase: bool = True,
    remove_stopwords: bool = False,
) -> list[str]:
    """
    Preprocess a text string into a list of lemmatized tokens.

    Args:
        text (str): The input text to preprocess.
        spacy_pipeline (str | spacy.Language): Either the name of a spaCy pipeline
            (e.g. "en_core_web_sm") or an already-loaded `spacy.Language` object.
        uppercase (bool): If True, convert all lemmas to uppercase. Default is True.
        remove_stopwords (bool): If True, remove stopwords before lemmatization. Default is False.

    Returns:
        list[str]: A list of lemmatized words (as strings), filtered to alphabetic tokens.

    """
    # Load the spaCy NLP pipeline if given as a string
    if isinstance(spacy_pipeline, str):
        nlp = spacy.load(spacy_pipeline)
    else:
        nlp = spacy_pipeline

    # Process the input text into tokens using spaCy
    doc = nlp(text)

    # Optionally filter out stopwords
    if remove_stopwords:
        doc = [token for token in doc if not token.is_stop]

    # Extract lemmas of alphabetic tokens (ignore numbers, punctuation, etc.)
    text_lemmas = [token.lemma_ for token in doc if token.is_alpha]

    # Optionally convert lemmas to uppercase
    if uppercase:
        text_lemmas = [l.upper() for l in text_lemmas]

    return text_lemmas


def preprocess_texts(
    texts: list[str], spacy_pipeline: str | spacy.Language = "en_core_web_sm", uppercase=True, remove_stopwords=False
) -> list[list[str]]:
    """
    Preprocess a list of text strings into a list of lemmatized token lists.

    Args:
        texts (list[str]): A list of input text strings.
        spacy_pipeline (str | spacy.Language): Either the name of a spaCy pipeline
            (e.g. "en_core_web_sm") or an already-loaded `spacy.Language` object.
        uppercase (bool): If True, convert all lemmas to uppercase. Default is True.
        remove_stopwords (bool): If True, remove stopwords before lemmatization. Default is False.

    Returns:
        list[list[str]]: A list where each element is a list of lemmatized tokens from the corresponding input text.

    """
    # Load the spaCy NLP pipeline if given as a string
    if isinstance(spacy_pipeline, str):
        nlp = spacy.load(spacy_pipeline)
    else:
        nlp = spacy_pipeline

    lemmas_for_all_texts = []

    for text in texts:
        # Reuse the already-loaded `nlp` pipeline for efficiency
        text_lemmas = preprocess_text(text, nlp, uppercase)
        lemmas_for_all_texts.append(text_lemmas)

    return lemmas_for_all_texts


def get_glosses_from_text(text: str, glosses: set[str], remove_stopwords=False) -> list[str]:
    """
    Extract glosses (lemmas) from the input text that match a known set of glosses.

    Args:
        text (str): The input text string to analyze.
        glosses (set[str]): A set of valid gloss terms to match against.
        remove_stopwords (bool, optional): Whether to remove stopwords before matching.
                                           Defaults to False.

    Returns:
        list[str]: A list of glosses found in the text, preserving their order of appearance.

    """
    # Lemmatize and optionally remove stopwords from the text
    text_lemmas = preprocess_text(text, remove_stopwords=remove_stopwords)

    # Return all lemmas that are in the known glosses set
    found_glosses = [lemma for lemma in text_lemmas if lemma in glosses]
    return found_glosses


def get_glosses_set_from_text(text: str, glosses: set[str], remove_stopwords=False) -> set[str]:
    """
    Get a unique set of glosses found in the input text.

    Args:
        text (str): The input text string to analyze.
        glosses (set[str]): A set of valid gloss terms to match against.
        remove_stopwords (bool, optional): Whether to remove stopwords before matching.
                                           Defaults to False.

    Returns:
        set[str]: A set of unique glosses found in the text.

    """
    return set(get_glosses_from_text(text=text, glosses=glosses, remove_stopwords=remove_stopwords))
