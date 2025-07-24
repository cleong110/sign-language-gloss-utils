from pathlib import Path

import pandas as pd


class DatasetDFCol:
    """Standardized column names"""

    VIDEO_ID = "VIDEO_ID"
    SPLIT = "SPLIT"
    GLOSS = "GLOSS"
    PARTICIPANT_ID = "PARTICIPANT_ID"
    DATASET = "DATASET"


def combine_dataset_dfs(dataset_df_files: list[Path], splits: list[str], filter_en_vocab: bool = False):
    dfs = []
    for file_path in dataset_df_files:
        if file_path.exists():
            print(f"✅ Found: {file_path}")
            df = pd.read_csv(
                file_path,
                dtype={
                    DatasetDFCol.GLOSS: str,
                    DatasetDFCol.SPLIT: str,
                    DatasetDFCol.VIDEO_ID: str,
                    DatasetDFCol.POSE_FILE_PATH: str,
                },
            )
            print(f"Loaded {len(df)} rows")
            df = df[df[DatasetDFCol.SPLIT].isin(splits)]
            df[DatasetDFCol.DATASET] = file_path.stem
            print(f"Loaded {len(df)} rows from splits: {splits}")
            print(f"There are {len(df[DatasetDFCol.GLOSS].unique())} unique glosses")
            dfs.append(df)
        else:
            print(f"❌ Missing: {file_path}")
    df = pd.concat(dfs)
    if DatasetDFCol.VIDEO_FILE_PATH in df.columns:
        df = df.drop(columns=[DatasetDFCol.VIDEO_FILE_PATH])

    df = df.dropna()

    if filter_en_vocab:
        df = df[~df[DatasetDFCol.GLOSS].str.contains("EN:", na=False)]
    print(f"Loaded {len(df)} rows total, from {len(dataset_df_files)} files")
    return df


def df_to_standardized_df(
    df: pd.DataFrame,
    video_id_col="video_id",
    split_col="split",
    gloss_col="gloss",
    signer_id_col="signer_id",
):
    """Standardize to specific predictable names: "Video ID" or "video_id" for example,  becomes "VIDEO_ID"""
    df = df.rename(
        columns={
            video_id_col: DatasetDFCol.VIDEO_ID,
            split_col: DatasetDFCol.SPLIT,
            gloss_col: DatasetDFCol.GLOSS,
            signer_id_col: DatasetDFCol.PARTICIPANT_ID,
        }
    )

    # rename all columns to CAPITAL_UNDERSCORE format
    # Rename columns to uppercase with underscores
    df.columns = [col.replace(" ", "_").upper() for col in df.columns]

    # capitalize all glosses
    df[DatasetDFCol.GLOSS] = df[DatasetDFCol.GLOSS].str.upper()

    # lowercase all splits
    df[DatasetDFCol.SPLIT] = df[DatasetDFCol.SPLIT].str.lower()

    return df
