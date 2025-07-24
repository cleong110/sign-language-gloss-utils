"""Abstract class for Vocab class which parses vocab from dataset"""

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class SignDatasetVocab(ABC):
    DATASET_NAME = None

    @abstractmethod
    def __init__(self, meta_path: Path | None):
        pass

    @abstractmethod
    def _load_metadata(self, meta_path: Path) -> pd.DataFrame:
        """Parses metadata to a dataframe with DatasetDF.GLOSS column"""
        pass

    def get_vocab(self) -> list[str]:
        return self.vocab

    def get_name(self) -> str:
        return self.DATASET_NAME

    @abstractmethod
    def _get_table(self) -> pd.DataFrame:
        pass
