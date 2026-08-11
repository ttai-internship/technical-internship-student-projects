from collections.abc import Iterable

from .validator import Issue


def clean_rows(rows: list[dict[str, str]], issues: Iterable[Issue]) -> list[dict[str, str]]:
    """Student Core: remove or repair rows according to documented rules."""
    # The starter's default policy is deliberately explicit: keep only rows
    # without a reported issue. Students may choose a repair policy, but must
    # document the change and preserve the raw input.
    invalid_rows = {issue.row_number for issue in issues}
    return [
        dict(row)
        for index, row in enumerate(rows, start=2)
        if index not in invalid_rows
    ]
