import unittest

from paper_reproduction.experiment import make_data, run_variant


class PaperReproductionPublicTests(unittest.TestCase):
    def test_data_generation_is_reproducible(self) -> None:
        self.assertEqual(make_data(), make_data())

    def test_baseline_result_has_required_fields(self) -> None:
        result = run_variant(make_data(), "baseline")
        self.assertEqual(result["variant"], "baseline")
        self.assertIn("accuracy", result)


if __name__ == "__main__":
    unittest.main()
