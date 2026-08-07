import json
from pathlib import Path

from .validator import Issue


def build_summary(rows: list[dict[str, str]], issue_count: int) -> dict:
    numeric_amounts = []
    for row in rows:
        try:
            numeric_amounts.append(float(row["amount"]))
        except (KeyError, TypeError, ValueError):
            continue
    return {
        "row_count": len(rows),
        "numeric_amount_count": len(numeric_amounts),
        "amount_total": round(sum(numeric_amounts), 2),
        "issue_count": issue_count,
    }


def write_json(summary: dict, path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def render_markdown(summary: dict, issues: list[Issue]) -> str:
    """Render a small human-readable report from the same summary contract."""
    lines = [
        "# Data quality report",
        "",
        f"- Rows after cleaning: {summary['row_count']}",
        f"- Numeric amounts: {summary['numeric_amount_count']}",
        f"- Amount total: {summary['amount_total']}",
        f"- Issues found: {summary['issue_count']}",
        "",
        "## Issues",
    ]
    if issues:
        lines.extend(
            f"- row {issue.row_number}, `{issue.field}`: {issue.message}" for issue in issues
        )
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


def write_markdown(summary: dict, issues: list[Issue], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_markdown(summary, issues), encoding="utf-8")
