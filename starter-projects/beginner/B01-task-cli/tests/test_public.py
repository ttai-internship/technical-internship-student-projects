import json
import tempfile
import unittest
from pathlib import Path

from task_cli.service import TaskService
from task_cli.storage import JsonStorage


class TaskServicePublicTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "tasks.json"
        self.service = TaskService(JsonStorage(self.path))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_and_list_persist(self) -> None:
        created = self.service.add("read the README")
        self.assertEqual(created.id, 1)
        self.assertEqual([task.title for task in self.service.list()], ["read the README"])

        reloaded = TaskService(JsonStorage(self.path))
        self.assertEqual(reloaded.list()[0].title, "read the README")

    def test_empty_title_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.service.add("   ")

    def test_storage_is_json(self) -> None:
        self.service.add("inspect output")
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(payload[0]["completed"], False)


if __name__ == "__main__":
    unittest.main()
