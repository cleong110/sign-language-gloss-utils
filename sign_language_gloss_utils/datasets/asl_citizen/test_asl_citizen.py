"""Test ASL Citizen"""

from pathlib import Path

from sign_language_gloss_utils.datasets import DatasetDFCol
from sign_language_gloss_utils.datasets.asl_citizen.asl_citizen import ASLCitizenDatasetVocab


# weird things to account for:
# ASL Citizen Test Set has 2731 vocab
# Non-alphanumeric characters for THIS/IT: {'/'}
# Non-alphanumeric characters for SKI-CA: {'-'}
# Non-alphanumeric characters for WALK-TIGHTROPE-CL: {'-'}
# Non-alphanumeric characters for HURDLE/TRIP1: {'/'}
# Non-alphanumeric characters for W.H.A.T: {'.'}
# Non-alphanumeric characters for STRETCH-CA: {'-'}
# Non-alphanumeric characters for A-LINEBOB: {'-'}
# Non-alphanumeric characters for TOOTHBRUSH-CA: {'-'}
# Non-alphanumeric characters for SPLASH-CA: {'-'}
# Non-alphanumeric characters for STAND-UP: {'-'}
# Non-alphanumeric characters for HURDLE/TRIP2: {'/'}
# Complete set: {'/', '-', '.'}
def test_asl_citizen_get_vocab():
    """Test Code"""
    csv_path = Path(__file__).parent / "test_files" / "train.csv"

    aslcitizenvocab = ASLCitizenDatasetVocab(csv_path)
    df = aslcitizenvocab._get_table()

    assert df[DatasetDFCol.SPLIT].unique().tolist()[0] == "train"
    assert len(df[DatasetDFCol.SPLIT].unique()) == 1

    vocab = aslcitizenvocab.get_vocab()
    assert len(vocab) == 10, f"vocab wrong length! ({len(vocab)}! {vocab}"
