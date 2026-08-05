def exact_match(expected: str, answer: str) -> bool:
    return expected.strip().lower() == answer.strip().lower()


def contains_expected(expected: str, answer: str) -> bool:
    return expected.strip().lower() in answer.strip().lower()


def evaluate(cases: list[dict], metric=contains_expected) -> dict:
    results = []
    for case in cases:
        passed = bool(metric(case["expected"], case["answer"]))
        results.append({"id": case["id"], "passed": passed})
    return {
        "count": len(results),
        "passed": sum(item["passed"] for item in results),
        "results": results,
    }
