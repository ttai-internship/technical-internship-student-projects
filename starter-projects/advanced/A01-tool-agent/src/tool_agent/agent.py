from collections.abc import Callable

from .tools import Tool


class ToolAgent:
    def __init__(self, tools: dict[str, Tool], model: Callable[[str], dict]) -> None:
        self.tools = tools
        self.model = model
        self.logs: list[dict] = []

    def run(self, prompt: str) -> str:
        decision = self.model(prompt)
        self.logs.append({"prompt": prompt, "decision": decision})
        if decision.get("type") == "answer":
            return str(decision.get("content", ""))
        if decision.get("type") != "tool_call":
            raise ValueError("model decision must be answer or tool_call")

        name = decision.get("name")
        tool = self.tools.get(name)
        if tool is None:
            raise ValueError(f"unknown tool: {name}")
        arguments = decision.get("arguments", {})
        if not isinstance(arguments, dict):
            raise ValueError("tool arguments must be an object")
        try:
            result = tool.handler(**arguments)
        except (TypeError, ValueError) as exc:
            self.logs.append({"tool": name, "error": str(exc)})
            raise ValueError(f"tool failed: {exc}") from exc
        self.logs.append({"tool": name, "result": result})
        return str(result)
