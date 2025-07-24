import argparse
from pathlib import Path

import pandas as pd

from sign_language_gloss_utils.datasets import DatasetDFCol
from sign_language_gloss_utils.datasets.asl_citizen.asl_citizen import ASLCitizenDatasetSplit


def save_aslcitizen_vocab(meta_path: Path, vocab_out: Path):
    print(f"Meta path: {meta_path.resolve()}")
    print(f"Vocab output path: {vocab_out.resolve()}")
    # Add your logic here

    split = ASLCitizenDatasetSplit(meta_path)
    # dict of lists to Dataframe to CSV
    vocab_df = pd.DataFrame({DatasetDFCol.GLOSS: split.get_vocab()})
    vocab_df.to_csv(vocab_out, index=False)


if __name__ == "__main__":
    default_out = Path(__file__).parent / "saved_vocab" / "vocab.csv"
    parser = argparse.ArgumentParser(description="Script using meta and vocab paths.")

    parser.add_argument("--meta-file", type=Path, required=True, help="Path to metadata file (e.g. train.csv)")

    parser.add_argument("--vocab_out", type=Path, default=default_out, help="CSV output path for vocab file")

    args = parser.parse_args()
    save_aslcitizen_vocab(meta_path=args.meta_file, vocab_out=args.vocab_out)
