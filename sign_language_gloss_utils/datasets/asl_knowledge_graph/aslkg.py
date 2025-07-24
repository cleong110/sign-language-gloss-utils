from sign_language_gloss_utils.datasets import DatasetDFCol
from sign_language_gloss_utils.datasets.dataset import SignDatasetVocab


class ASLKG(SignDatasetVocab):
    raise NotImplementedError("TODO!")


def convert_eng_to_ase_gloss_translations(df, asl_knowledge_graph_df, translations_only=False):
    translation_df = asl_knowledge_graph_df[asl_knowledge_graph_df["relation"] == "has_translation"]

    translation_df.loc[:, "object"] = translation_df["object"].str.upper()

    matching_translations = translation_df[translation_df["object"].isin(df[DatasetDFCol.GLOSS])]

    selected_translations = []
    for translated_word in matching_translations["object"].unique():
        translations = matching_translations[matching_translations["object"] == translated_word]
        translations_without_colon = []
        for translation in translations["subject"].tolist():
            translation = translation.split(":")[-1].upper()
            translations_without_colon.append(translation)

        if len(set(translations_without_colon)) == 1:
            translated_word_without_lang = translated_word.split(":")[1]
            translation = next(iter(set(translations_without_colon)))

            if translated_word_without_lang == translation:
                selected_translations.append((translated_word, translation))

    mapping_dict = dict(selected_translations)

    if translations_only:
        # Filter rows where GLOSS is in the mapping keys
        df = df[df[DatasetDFCol.GLOSS].isin(mapping_dict)].copy()

    # Apply the mapping safely using .loc
    df.loc[:, DatasetDFCol.GLOSS] = df[DatasetDFCol.GLOSS].map(mapping_dict).fillna(df[DatasetDFCol.GLOSS])
    return df
