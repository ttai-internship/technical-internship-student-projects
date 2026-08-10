import argparse
import json
from pathlib import Path

from .data import load_dataset
from .evaluate import evaluate
from .model import MajorityClassifier, build_student_model

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=["baseline", "student"], default="baseline")
    args = parser.parse_args()

    train_x, train_y = load_dataset(ROOT / "data" / "train.csv")
    test_x, test_y = load_dataset(ROOT / "data" / "test.csv")
    model = MajorityClassifier() if args.model == "baseline" else build_student_model()
    if args.model == "baseline":
        model.fit(train_y)
    else:
        model.fit(train_x, train_y)
    print(json.dumps(evaluate(model, test_x, test_y), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
