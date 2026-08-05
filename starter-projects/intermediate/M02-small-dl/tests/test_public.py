import unittest

import torch

from small_dl.data import make_dataset
from small_dl.model import TinyMLP


class SmallDLPublicTests(unittest.TestCase):
    def test_dataset_shape(self) -> None:
        features, labels = make_dataset()[0]
        self.assertEqual(tuple(features.shape), (2,))
        self.assertIn(int(labels), {0, 1})

    def test_model_output_shape(self) -> None:
        output = TinyMLP()(torch.zeros((4, 2)))
        self.assertEqual(tuple(output.shape), (4, 2))


if __name__ == "__main__":
    unittest.main()
