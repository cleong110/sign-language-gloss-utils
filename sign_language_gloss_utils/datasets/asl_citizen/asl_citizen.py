from pathlib import Path

import pandas as pd

from sign_language_gloss_utils.datasets import DatasetDFCol
from sign_language_gloss_utils.datasets.dataset import SignDatasetVocab
from sign_language_gloss_utils.datasets.dataset_parsing.dataset_utils import df_to_standardized_df


class ASLCitizenDatasetVocab(SignDatasetVocab):
    """Can parse metadata to vocab, or just return saved"""

    DATASET_NAME = "asl-citizen"
    VIDEO_FILE_COL_NAME = "Video file"
    PARTICIPANT_ID_COL_NAME = "Participant ID"
    GLOSS_COL_NAME = "Gloss"
    ASLLEX_CODE_COL_NAME = "ASL-LEX Code"

    def __init__(self, meta_path: Path | None):
        """Setup the class by loading metadata and getting the vocab out"""
        if meta_path is not None:
            df = self._load_metadata(meta_path)
            self.df = df
            self.vocab = df[DatasetDFCol.GLOSS].unique().tolist()
        else:
            self.df = pd.DataFrame()
            self.vocab = self._load_saved_vocab()

    def _load_metadata(self, csv_path: Path) -> pd.DataFrame:
        """Loads train.csv, etc for ASL Citizen, with splits and video IDs added"""
        split_name = csv_path.stem
        assert split_name in ["train", "val", "test"]
        df = pd.read_csv(csv_path, header=0)
        df[DatasetDFCol.DATASET] = self.DATASET_NAME
        df[DatasetDFCol.SPLIT] = split_name
        # Create Video ID
        df[DatasetDFCol.VIDEO_ID] = df[self.VIDEO_FILE_COL_NAME].apply(lambda x: Path(x).stem.split("-")[0])
        df = df_to_standardized_df(
            df, video_id_col=DatasetDFCol.VIDEO_ID, split_col=DatasetDFCol.SPLIT, signer_id_col="Participant ID"
        )
        # TODO: 4.7299129501965353e-7-seedSOUR.mp4, does that cause issues?
        return df

    def _get_table(self) -> pd.DataFrame:
        """Get the df"""
        return self.df

    def _load_saved_vocab(self) -> list:
        csv_path = Path(__file__).parent / "saved_vocab" / "vocab.csv"
        df = pd.read_csv(csv_path)
        return df[DatasetDFCol.GLOSS].tolist()
