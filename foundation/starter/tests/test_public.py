import unittest

from foundation_lab.lesson01 import greeting
from foundation_lab.lesson02 import receipt, total_price
from foundation_lab.lesson03 import classify_score, sum_numbers
from foundation_lab.lesson04 import describe_count, repeat_message


class FoundationPublicTests(unittest.TestCase):
    def test_greeting(self) -> None:
        self.assertEqual(greeting("Ada"), "Hello, Ada!")

    def test_total_price(self) -> None:
        self.assertEqual(total_price(2.5, 4), 10.0)

    def test_receipt_formats_total(self) -> None:
        self.assertEqual(receipt("pen", 1.2, 3), "pen: 3.60")

    def test_score_boundaries(self) -> None:
        self.assertEqual(classify_score(90), "excellent")
        self.assertEqual(classify_score(60), "pass")
        self.assertEqual(classify_score(59), "retry")

    def test_sum_numbers(self) -> None:
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([1, 2, 3]), 6)

    def test_repeat_message(self) -> None:
        self.assertEqual(repeat_message("go", 3), ["go", "go", "go"])

    def test_describe_count(self) -> None:
        self.assertEqual(describe_count(["a", "b"]), "count=2")


if __name__ == "__main__":
    unittest.main()
