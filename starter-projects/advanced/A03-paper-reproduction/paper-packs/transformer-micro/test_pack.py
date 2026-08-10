import unittest

from run import run


class TransformerMicroTests(unittest.TestCase):
    def test_attention_rows_are_probability_distributions(self):
        result = run()
        self.assertEqual(result["attention_shape"], [3, 3])
        self.assertEqual(result["row_sums"], [1.0, 1.0, 1.0])


if __name__ == "__main__":
    unittest.main()
