def repeat_message(message: str, times: int) -> list[str]:
    result: list[str] = []
    for _ in range(times):
        result.append(message)
    return result


def describe_count(items: list[str]) -> str:
    return f"count={len(items)}"


def main() -> None:
    print(repeat_message("practice", 2))


if __name__ == "__main__":
    main()
