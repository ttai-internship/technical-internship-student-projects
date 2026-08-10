"""Load the fixed, offline evaluation cases for A02."""

from __future__ import annotations

import json
from pathlib import Path

CASES_PATH = Path(__file__).resolve().parents[2] / "eval" / "cases.json"
CASES = json.loads(CASES_PATH.read_text(encoding="utf-8"))
