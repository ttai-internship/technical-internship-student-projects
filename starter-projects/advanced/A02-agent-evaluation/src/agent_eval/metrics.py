from collections.abc import Callable


def exact_match(expected: str, answer: str) -> bool:
    return expected.strip().lower() == answer.strip().lower()


def contains_expected(expected: str, answer: str) -> bool:
    return expected.strip().lower() in answer.strip().lower()


def classify_failure(case: dict, passed: bool) -> str:
    if passed:
        return "pass"
    failure_type = str(case.get("failure_type", "other"))
    allowed = {"retrieval", "generation", "understanding", "other"}
    return failure_type if failure_type in allowed else "other"


def evaluate(
    cases: list[dict],
    metric: Callable[[str, str], bool] = contains_expected,
) -> dict:
    results = []
    for case in cases:
        passed = bool(metric(case["expected"], case["answer"]))
        results.append(
            {
                "id": case["id"],
                "passed": passed,
                "failure_type": classify_failure(case, passed),
            }
        )
    failure_counts: dict[str, int] = {}
    for item in results:
        if item["failure_type"] != "pass":
            failure_counts[item["failure_type"]] = failure_counts.get(item["failure_type"], 0) + 1
    return {
        "count": len(results),
        "passed": sum(item["passed"] for item in results),
        "pass_rate": sum(item["passed"] for item in results) / len(results) if results else 0.0,
        "failure_counts": failure_counts,
        "results": results,
    }
