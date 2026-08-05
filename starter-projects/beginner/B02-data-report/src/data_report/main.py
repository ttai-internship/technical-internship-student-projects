import argparse

from .cleaner import clean_rows
from .reader import read_rows
from .report import build_summary, write_json
from .validator import find_issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean a CSV and write a summary")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = read_rows(args.input)
    issues = find_issues(rows)
    cleaned = clean_rows(rows, issues)
    write_json(build_summary(cleaned, len(issues)), args.output)
    print(f"rows={len(rows)} issues={len(issues)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
