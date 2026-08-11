"""Run every ready A03 paper micro-pack using only local CPU inputs."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "starter-projects" / "advanced" / "A03-paper-reproduction" / "paper-packs"
CATALOG_PATH = PACK_ROOT / "catalog.json"


def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    failures: list[str] = []
    for entry in catalog["packs"]:
        if entry.get("ready_for_assignment") is not True:
            continue
        pack_id = entry["id"]
        pack_path = PACK_ROOT / pack_id
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(
            value for value in (str(pack_path), env.get("PYTHONPATH")) if value
        )
        print(f"=== {pack_id} ===")
        for command in (
            [sys.executable, "run.py"],
            [sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_pack.py", "-v"],
        ):
            completed = subprocess.run(
                command,
                cwd=pack_path,
                env=env,
                capture_output=True,
                text=True,
                check=False,
                timeout=60,
            )
            if completed.stdout:
                print(completed.stdout.rstrip())
            if completed.stderr:
                print(completed.stderr.rstrip(), file=sys.stderr)
            if completed.returncode != 0:
                failures.append(f"{pack_id}: {' '.join(command)}")
                break
    if failures:
        for failure in failures:
            print(f"ERROR {failure}", file=sys.stderr)
        return 1
    print("All ready A03 paper packs passed their local CPU checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
