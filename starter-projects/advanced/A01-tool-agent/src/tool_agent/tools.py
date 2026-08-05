from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[..., str]


def get_ticket(ticket_id: int) -> str:
    tickets = {1: "open: prepare onboarding", 2: "closed: review README"}
    return tickets.get(ticket_id, "ticket not found")


def list_tools() -> dict[str, Tool]:
    return {
        "get_ticket": Tool(
            name="get_ticket",
            description="Get a ticket by integer id",
            handler=get_ticket,
        )
    }
