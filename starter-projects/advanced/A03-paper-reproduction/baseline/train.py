"""Run the locked baseline for the selected paper pack."""

from paper_reproduction.experiment import make_data, run_variant


def main() -> int:
    result = run_variant(make_data(seed=7, size=20), "baseline")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
