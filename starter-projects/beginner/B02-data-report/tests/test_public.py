import unittest
from pathlib import Path

from data_report.reader import read_rows
from data_report.report import build_summary


class DataReportPublicTests(unittest.TestCase):
    def test_reader_loads_csv_rows(self) -> None:
        path = Path(__file__).parents[1] / "data" / "raw" / "sample.csv"
        rows = read_rows(path)
        self.assertEqual(len(rows), 6)
        self.assertEqual(rows[0]["order_id"], "1001")

    def test_summary_is_deterministic(self) -> None:
        rows = [{"amount": "2.5"}, {"amount": "3.0"}, {"amount": "bad"}]
        self.assertEqual(
            build_summary(rows, issue_count=1),
            {
                "row_count": 3,
                "numeric_amount_count": 2,
                "amount_total": 5.5,
                "issue_count": 1,
            },
        )


if __name__ == "__main__":
    unittest.main()
