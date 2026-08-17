"""Scan tracked text files for high-confidence credential signatures."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache"}
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,})"),
    "AWS access key": re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}


def candidate_files() -> list[Path]:
    try:
        completed = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return [path for path in ROOT.rglob("*") if path.is_file()]
    return [ROOT / item.decode("utf-8") for item in completed.stdout.split(b"\0") if item]


def scan() -> list[str]:
    findings: list[str] = []
    for path in candidate_files():
        if not path.is_file() or SKIP_PARTS.intersection(path.parts) or path.stat().st_size > 2_000_000:
            continue
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\0" in raw:
            continue
        text = raw.decode("utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for name, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{line_number}: possible {name}")
    return findings


def main() -> int:
    findings = scan()
    if findings:
        for finding in findings:
            print(f"ERROR {finding}", file=sys.stderr)
        return 1
    print("No high-confidence credential signatures found in tracked files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
