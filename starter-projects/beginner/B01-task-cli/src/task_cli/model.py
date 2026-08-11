from dataclasses import asdict, dataclass
from datetime import UTC, datetime


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    created_at: str = ""

    @classmethod
    def new(cls, task_id: int, title: str) -> "Task":
        return cls(
            id=task_id,
            title=title,
            created_at=datetime.now(UTC).isoformat(),
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict) -> "Task":
        return cls(
            id=int(value["id"]),
            title=str(value["title"]),
            completed=bool(value.get("completed", False)),
            created_at=str(value.get("created_at", "")),
        )
