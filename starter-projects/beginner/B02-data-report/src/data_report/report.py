import json
from pathlib import Path


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
