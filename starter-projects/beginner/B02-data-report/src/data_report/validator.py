from dataclasses import dataclass


@dataclass(frozen=True)
class Issue:
    row_number: int
    field: str
    message: str


ALLOWED_STATUS = {"paid", "pending", "cancelled"}


def find_issues(rows: list[dict[str, str]]) -> list[Issue]:
    """Return data-quality issues without changing the input rows."""
    issues: list[Issue] = []
    seen_ids: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        order_id = row.get("order_id", "").strip()
        if not order_id:
            issues.append(Issue(row_number, "order_id", "missing order id"))
        elif order_id in seen_ids:
            issues.append(Issue(row_number, "order_id", "duplicate order id"))
        seen_ids.add(order_id)

        if not row.get("customer", "").strip():
            issues.append(Issue(row_number, "customer", "missing customer"))

        try:
            amount = float(row.get("amount", ""))
            if amount < 0:
                issues.append(Issue(row_number, "amount", "amount cannot be negative"))
        except ValueError:
            issues.append(Issue(row_number, "amount", "amount is not numeric"))

        if row.get("status", "").strip() not in ALLOWED_STATUS:
            issues.append(Issue(row_number, "status", "unknown status"))
    return issues
