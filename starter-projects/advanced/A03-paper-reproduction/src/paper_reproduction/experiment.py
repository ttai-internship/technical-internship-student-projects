import random


def make_data(seed: int = 7, size: int = 20) -> list[tuple[float, int]]:
    randomizer = random.Random(seed)
    return [(randomizer.random(), index % 2) for index in range(size)]


def run_variant(data: list[tuple[float, int]], variant: str = "baseline") -> dict:
    """Return a deterministic toy result until a real paper is selected."""
    if variant not in {"baseline", "student"}:
        raise ValueError("variant must be baseline or student")
    threshold = 0.5 if variant == "baseline" else 0.6
    predictions = [int(value >= threshold) for value, _label in data]
    labels = [label for _value, label in data]
    correct = sum(prediction == label for prediction, label in zip(predictions, labels))
    return {"variant": variant, "threshold": threshold, "accuracy": correct / len(labels)}
