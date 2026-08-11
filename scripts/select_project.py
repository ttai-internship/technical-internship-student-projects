"""Record a pseudonymous self-study selection in the public repository.

Formal cohort assignments use GitHub Classroom and do not require this file.
The public command remains useful for local practice and preserves B00 as a
foundation gate before a later B01/B02/B03 primary project.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "projects.json"
PROJECT_IDS = ("B00", "B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03")
DURATIONS = ("one-week", "one-month", "two-month", "half-year")


def load_entry(project_id: str) -> dict[str, object]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if project_id == "B00":
        return manifest["foundation"]
    return next(project for project in manifest["projects"] if project["id"] == project_id)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", choices=PROJECT_IDS, required=True)
    parser.add_argument(
        "--assignment-id",
        default="local-self-study",
        help="pseudonymous local label; do not use a real name or student number",
    )
    parser.add_argument("--duration", choices=DURATIONS, default="one-week")
    args = parser.parse_args()

    if not args.assignment_id.replace("-", "").replace("_", "").replace(".", "").isalnum():
        parser.error("--assignment-id must be a pseudonymous label using letters, numbers, '-', '_' or '.'")

    selection_path = ROOT / "PROJECT_SELECTION.json"
    existing: dict[str, object] = {}
    if selection_path.exists():
        try:
            existing = json.loads(selection_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            parser.error(f"invalid existing PROJECT_SELECTION.json: {error}")

    entry = load_entry(args.project)
    if entry.get("assignable", True) is False:
        parser.error("this project is a research preview and is not assignable until its paper pack is locked")
    previous_primary = existing.get("primary_project")
    if isinstance(previous_primary, dict) and previous_primary.get("project_id") not in {None, args.project}:
        parser.error("a different primary project is already selected; edit the selection deliberately before switching")

    foundation_completed = bool(existing.get("foundation_completed", False)) or args.project == "B00"
    primary = previous_primary if isinstance(previous_primary, dict) else None
    if args.project != "B00":
        primary = {
            "project_id": entry["id"],
            "level": entry["level"],
            "title": entry["title"],
            "duration": args.duration,
            "task": entry["task"],
            "starter": entry["starter"],
            "notebook": entry["notebook"],
        }

    selection = {
        "schema_version": 2,
        "assignment_id": args.assignment_id,
        "foundation_completed": foundation_completed,
        "primary_project": primary,
        "branch_pattern": "feature/<project>-<slice>",
    }
    selection_path.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.project == "B00":
        print("Recorded B00 foundation completion route.")
    else:
        print(f"Selected primary project {entry['id']}: {entry['title']}")
    print(f"Foundation completed: {foundation_completed}")
    print("Formal cohort participants should use the private GitHub Classroom assignment repository.")
    print("Commit PROJECT_SELECTION.json only when its pseudonymous contents are safe to publish.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
