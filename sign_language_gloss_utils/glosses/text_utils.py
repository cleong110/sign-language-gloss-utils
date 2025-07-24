import spacy


def preprocess_text(text, spacy_pipeline: str | spacy.Language = "en_core_web_sm", uppercase=True) -> list[str]:
    """Given a text, preprocess to lemmas"""
    # English pipelines include a rule-based lemmatizer
    if isinstance(spacy_pipeline, str):
        nlp = spacy.load(spacy_pipeline)
    else:
        nlp = spacy_pipeline
    # not a set! We might want counts later
    doc = nlp(text)
    text_lemmas = [token.lemma_ for token in doc if token.is_alpha]
    if uppercase:
        text_lemmas = [l.upper() for l in text_lemmas]
    return text_lemmas


def preprocess_texts(
    texts: list[str], spacy_pipeline: str | spacy.Language = "en_core_web_sm", uppercase=True
) -> list[list[str]]:
    """Given a list of texts, preprocess to list of lists of lemmas"""
    # English pipelines include a rule-based lemmatizer
    if isinstance(spacy_pipeline, str):
        nlp = spacy.load(spacy_pipeline)
    else:
        nlp = spacy_pipeline
    # lemmatizer = nlp.get_pipe("lemmatizer")
    # print(lemmatizer.mode)  # 'rule'

    lemmas_for_all_texts = []
    for text in texts:
        text_lemmas = preprocess_text(text, nlp, uppercase)
        lemmas_for_all_texts.append(text_lemmas)

    return lemmas_for_all_texts


def get_glosses_set_from_text(text: str, glosses: set[str]) -> set[str]:
    text_lemmas = preprocess_text(text)
    found_glosses = {l for l in text_lemmas if l in glosses}
    return found_glosses


#     doc = nlp(text.lower())
#     lemmas = {token.lemma_.upper() for token in doc if token.is_alpha}
#     return glosses & lemmas
