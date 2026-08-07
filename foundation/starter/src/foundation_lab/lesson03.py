def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 60:
        return "pass"
    return "retry"


def sum_numbers(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


def main() -> None:
    print(classify_score(75))
    print(sum_numbers([1, 2, 3]))


if __name__ == "__main__":
    main()
