import unittest

from run import run


class ReActEvaluationTests(unittest.TestCase):
    def test_fixed_trace_has_one_failure(self):
        result = run()
        self.assertEqual(result["case_count"], 3)
        self.assertAlmostEqual(result["pass_rate"], 2 / 3)
        self.assertEqual(sum(item["passed"] for item in result["results"]), 2)


if __name__ == "__main__":
    unittest.main()
