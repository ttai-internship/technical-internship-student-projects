import json
from typing import Any

TICKETS: list[dict[str, Any]] = [
    {"id": 1, "title": "prepare onboarding", "status": "open"},
    {"id": 2, "title": "review README", "status": "closed"},
    {"id": 3, "title": "run CI", "status": "open"},
]


def filter_tickets(status: str | None = None) -> list[dict[str, Any]]:
    """Return tickets. Student Core: implement status filtering and validation."""
    del status
    return [dict(ticket) for ticket in TICKETS]


def encode_tickets(status: str | None = None) -> bytes:
    payload = {"items": filter_tickets(status), "count": len(filter_tickets(status))}
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")
