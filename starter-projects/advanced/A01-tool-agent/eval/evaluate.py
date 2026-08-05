"""Run the fixed, deterministic A01 cases and print a JSON report."""

from __future__ import annotations

import json
from pathlib import Path

from tool_agent.agent import ToolAgent
from tool_agent.fake_model import fake_model
from tool_agent.tools import list_tools

ROOT = Path(__file__).resolve().parents[1]


def load_cases(path: str | Path = ROOT / "eval" / "cases.json") -> list[dict[str, str]]:
    cases = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(cases, list) or len(cases) < 10:
        raise ValueError("A01 requires at least 10 fixed cases")
    return cases


def evaluate_cases(cases: list[dict[str, str]]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for case in cases:
        agent = ToolAgent(list_tools(), fake_model)
        try:
            result = agent.run(case["prompt"])
            passed = case["expected_contains"].lower() in result.lower()
            error = ""
        except (TypeError, ValueError, KeyError) as exc:
            result = ""
            passed = False
            error = str(exc)
        rows.append(
            {
                "id": case["id"],
                "passed": passed,
                "result": result,
                "error": error,
                "tool_calls": sum("tool" in item for item in agent.logs),
            }
        )
    return {
        "total": len(rows),
        "passed": sum(bool(row["passed"]) for row in rows),
        "failed": sum(not bool(row["passed"]) for row in rows),
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(evaluate_cases(load_cases()), ensure_ascii=False, indent=2))
