import argparse
from pathlib import Path

from .cleaner import clean_rows
from .reader import read_rows
from .report import build_summary, write_json, write_markdown
from .validator import find_issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean a CSV and write a summary")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--markdown-output")
    args = parser.parse_args()

    rows = read_rows(args.input)
    issues = find_issues(rows)
    cleaned = clean_rows(rows, issues)
    summary = build_summary(cleaned, len(issues))
    write_json(summary, args.output)
    markdown_output = args.markdown_output or str(Path(args.output).with_suffix(".md"))
    write_markdown(summary, issues, markdown_output)
    print(f"rows={len(rows)} issues={len(issues)} output={args.output} markdown={markdown_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
