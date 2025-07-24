from abc import ABC

import pandas as pd


class SignDataset(ABC):
    DATASET_NAME = None

    def __init__(self, meta_path):
        pass

    def _load_metadata(self, meta_path) -> pd.DataFrame:
        pass

    def get_vocab(self) -> list[str]:
        return self.vocab

    def get_name(self) -> str:
        return self.DATASET_NAME

    def get_table(self) -> pd.DataFrame:
        pass
