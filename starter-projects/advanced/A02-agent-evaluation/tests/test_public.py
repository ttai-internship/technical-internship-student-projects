import unittest

from agent_eval.metrics import contains_expected, evaluate


class AgentEvaluationPublicTests(unittest.TestCase):
    def test_contains_metric(self) -> None:
        self.assertTrue(contains_expected("Paris", "Paris is the answer"))
        self.assertFalse(contains_expected("Paris", "London"))

    def test_evaluation_counts_results(self) -> None:
        result = evaluate([
            {"id": "a", "expected": "yes", "answer": "yes"},
            {"id": "b", "expected": "no", "answer": "maybe"},
        ])
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["passed"], 1)


if __name__ == "__main__":
    unittest.main()
