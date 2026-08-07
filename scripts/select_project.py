"""Record one student's selected project in the public repository."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "projects.json"
PROJECT_IDS = ("B00", "B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03")
DURATIONS = ("one-week", "one-month", "two-month", "half-year")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", choices=PROJECT_IDS, required=True)
    parser.add_argument("--student-id", required=True)
    parser.add_argument("--duration", choices=DURATIONS, default="one-week")
    args = parser.parse_args()

    selection_path = ROOT / "PROJECT_SELECTION.json"
    if selection_path.exists():
        parser.error("PROJECT_SELECTION.json already exists; edit it deliberately before selecting again")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    entry = (
        manifest["foundation"]
        if args.project == "B00"
        else next(project for project in manifest["projects"] if project["id"] == args.project)
    )
    selection = {
        "schema_version": 1,
        "student_id": args.student_id,
        "project_id": entry["id"],
        "level": entry["level"],
        "duration": args.duration,
        "branch_pattern": f"feature/{args.project}-<slice>",
        "task": entry["task"],
        "starter": entry["starter"],
        "notebook": entry["notebook"],
    }
    selection_path.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Selected {entry['id']}: {entry['title']}")
    print(f"Task: {entry['task']}")
    print(f"Starter: {entry['starter']}")
    print(f"Notebook: {entry['notebook']}")
    print("Commit PROJECT_SELECTION.json, then implement only the selected Core.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
