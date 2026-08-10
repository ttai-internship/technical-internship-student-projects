from pathlib import Path

import pandas as pd

FEATURES = ["hours", "assignments", "attendance"]
TARGET = "passed"


def load_dataset(path: str | Path) -> tuple[pd.DataFrame, pd.Series]:
    frame = pd.read_csv(path)
    missing = set(FEATURES + [TARGET]) - set(frame.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    return frame[FEATURES], frame[TARGET]
