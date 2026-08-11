"""Evaluate deterministic ReAct-style tool traces without an online model."""

from __future__ import annotations

import json

CASES = [
    {
        "id": "lookup_then_answer",
        "expected": ["search", "answer"],
        "trace": [{"action": "search"}, {"action": "answer"}],
    },
    {
        "id": "calculator_then_answer",
        "expected": ["calculator", "answer"],
        "trace": [{"action": "calculator"}, {"action": "answer"}],
    },
    {
        "id": "missing_tool",
        "expected": ["search", "answer"],
        "trace": [{"action": "answer"}],
    },
]


def evaluate_case(case: dict[str, object]) -> dict[str, object]:
    trace = case["trace"]
    expected = case["expected"]
    actual = [step["action"] for step in trace]
    return {
        "case_id": case["id"],
        "passed": actual == expected,
        "expected_actions": expected,
        "actual_actions": actual,
        "failure_type": None if actual == expected else "wrong_tool_sequence",
    }


def run() -> dict[str, object]:
    results = [evaluate_case(case) for case in CASES]
    return {
        "pack_id": "react-eval",
        "case_count": len(results),
        "pass_rate": sum(result["passed"] for result in results) / len(results),
        "results": results,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
