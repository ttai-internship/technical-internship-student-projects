import unittest
from pathlib import Path

from tabular_ml.data import FEATURES, load_dataset
from tabular_ml.model import MajorityClassifier


class TabularMLPublicTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(__file__).parents[1]

    def test_dataset_schema_is_stable(self) -> None:
        features, labels = load_dataset(self.root / "data" / "train.csv")
        self.assertEqual(list(features.columns), FEATURES)
        self.assertEqual(len(features), len(labels))

    def test_majority_baseline_is_deterministic(self) -> None:
        model = MajorityClassifier().fit([0, 1, 1, 0, 1])
        self.assertEqual(model.predict([[1], [2]]), [1, 1])


if __name__ == "__main__":
    unittest.main()
