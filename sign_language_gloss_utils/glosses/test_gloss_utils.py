import pytest

from sign_language_gloss_utils.datasets import DATASET_NAMES
from sign_language_gloss_utils.glosses.gloss_utils import get_dataset_vocab


def test_get_vocab():
    implemented = ["asl-citizen"]
    for ds_name in DATASET_NAMES:
        if ds_name in implemented:
            vocab = get_dataset_vocab(ds_name)
            assert len(vocab) == 2731
        else:
            with pytest.raises(NotImplementedError, match=f"not implemented for {ds_name}") as e:
                vocab = get_dataset_vocab(ds_name)
