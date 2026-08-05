import json
import os
from pathlib import Path

from .model import Task


class JsonStorage:
    def __init__(self, path: str | Path | None = None) -> None:
        configured = path or os.environ.get("TASK_CLI_DATA", "tasks.json")
        self.path = Path(configured)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            raise ValueError("task data must be a JSON list")
        return [Task.from_dict(item) for item in raw]

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [task.to_dict() for task in tasks]
        self.path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
