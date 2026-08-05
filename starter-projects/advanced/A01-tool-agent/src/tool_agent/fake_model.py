def fake_model(prompt: str) -> dict:
    """Deterministic model substitute for tests and local learning."""
    if prompt.startswith("ticket:"):
        value = prompt.split(":", 1)[1].strip()
        try:
            ticket_id = int(value)
        except ValueError:
            return {"type": "answer", "content": "invalid ticket id"}
        return {
            "type": "tool_call",
            "name": "get_ticket",
            "arguments": {"ticket_id": ticket_id},
        }
    return {"type": "answer", "content": "I can answer without a tool."}
