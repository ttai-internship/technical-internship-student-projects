import json

from .agent import ToolAgent
from .fake_model import fake_model
from .tools import list_tools


def main() -> int:
    agent = ToolAgent(list_tools(), fake_model)
    result = agent.run("ticket: 1")
    print(json.dumps({"result": result, "logs": agent.logs}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
