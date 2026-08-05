from collections.abc import Iterable

from .validator import Issue


def clean_rows(rows: list[dict[str, str]], issues: Iterable[Issue]) -> list[dict[str, str]]:
    """Student Core: remove or repair rows according to documented rules."""
    # Baseline deliberately keeps the original rows. Students must decide and
    # document how duplicate, incomplete, invalid, and negative rows are handled.
    del issues
    return list(rows)
