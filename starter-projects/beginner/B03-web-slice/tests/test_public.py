import json
import unittest

from web_slice.app import encode_tickets, filter_tickets


class WebSlicePublicTests(unittest.TestCase):
    def test_default_returns_all_tickets(self) -> None:
        self.assertEqual(len(filter_tickets()), 3)

    def test_response_is_json_with_count(self) -> None:
        payload = json.loads(encode_tickets())
        self.assertEqual(payload["count"], len(payload["items"]))


if __name__ == "__main__":
    unittest.main()
