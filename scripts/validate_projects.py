"""Validate the repository-wide project contract without third-party packages."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "projects.json"
CATALOG_PATH = ROOT / "curriculum" / "catalog.json"
REQUIRED_FIELDS = {
    "id",
    "level",
    "title",
    "task",
    "starter",
    "notebook",
    "readme",
    "tests",
    "duration_core",
}
EXPECTED_IDS = {"B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03"}
EXPECTED_LEVELS = {"beginner", "intermediate", "advanced"}
FOUNDATION_REQUIRED_FIELDS = {
    "id",
    "level",
    "title",
    "task",
    "starter",
    "notebook",
    "readme",
    "tests",
    "duration_core",
}


def validate() -> list[str]:
    errors: list[str] = []
    if not MANIFEST_PATH.is_file():
        return [f"missing manifest: {MANIFEST_PATH.relative_to(ROOT)}"]

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"invalid JSON in manifest: {error}"]

    if not CATALOG_PATH.is_file():
        errors.append(f"missing curriculum catalog: {CATALOG_PATH.relative_to(ROOT)}")
    else:
        try:
            catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"invalid JSON in curriculum catalog: {error}")
        else:
            if catalog.get("schema_version") != 1:
                errors.append("curriculum catalog schema_version must be 1")
            if not isinstance(catalog.get("official_backbone"), list) or not catalog["official_backbone"]:
                errors.append("curriculum catalog official_backbone must be a non-empty list")
            if not isinstance(catalog.get("mentor_review"), list):
                errors.append("curriculum catalog mentor_review must be a list")

    projects = manifest.get("projects")
    if not isinstance(projects, list):
        return ["manifest.projects must be a list"]

    ids = [project.get("id") for project in projects if isinstance(project, dict)]
    if set(ids) != EXPECTED_IDS:
        errors.append(f"project IDs must be {sorted(EXPECTED_IDS)}, got {sorted(set(ids))}")
    if len(ids) != len(set(ids)):
        errors.append("project IDs must be unique")

    levels = Counter(project.get("level") for project in projects if isinstance(project, dict))
    if set(levels) != EXPECTED_LEVELS:
        errors.append(f"levels must be {sorted(EXPECTED_LEVELS)}, got {sorted(levels)}")
    for level in sorted(EXPECTED_LEVELS):
        if levels[level] != 3:
            errors.append(f"level {level!r} must contain exactly 3 projects")

    for project in projects:
        if not isinstance(project, dict):
            errors.append("each project entry must be an object")
            continue
        project_id = project.get("id", "<unknown>")
        missing = REQUIRED_FIELDS - project.keys()
        if missing:
            errors.append(f"{project_id}: missing fields {sorted(missing)}")
        if project.get("level") not in EXPECTED_LEVELS:
            errors.append(f"{project_id}: invalid level {project.get('level')!r}")
        if not isinstance(project.get("duration_core"), list) or not project["duration_core"]:
            errors.append(f"{project_id}: duration_core must be a non-empty list")

        for field in ("task", "starter", "notebook", "readme", "tests"):
            value = project.get(field)
            if not isinstance(value, str):
                continue
            path = ROOT / value
            if not path.exists():
                errors.append(f"{project_id}: {field} does not exist: {value}")

        starter = project.get("starter")
        if isinstance(starter, str) and not (ROOT / starter / "src").is_dir():
            errors.append(f"{project_id}: starter must contain src/: {starter}")

    foundation = manifest.get("foundation")
    if not isinstance(foundation, dict):
        errors.append("manifest.foundation must be an object")
    else:
        missing = FOUNDATION_REQUIRED_FIELDS - foundation.keys()
        if missing:
            errors.append(f"B00: missing fields {sorted(missing)}")
        if foundation.get("id") != "B00":
            errors.append(f"foundation id must be 'B00', got {foundation.get('id')!r}")
        if foundation.get("level") != "foundation":
            errors.append(f"B00: level must be 'foundation', got {foundation.get('level')!r}")
        if not isinstance(foundation.get("duration_core"), list) or not foundation["duration_core"]:
            errors.append("B00: duration_core must be a non-empty list")
        for field in ("task", "starter", "notebook", "readme", "tests"):
            value = foundation.get(field)
            if not isinstance(value, str):
                continue
            path = ROOT / value
            if not path.exists():
                errors.append(f"B00: {field} does not exist: {value}")
        starter = foundation.get("starter")
        if isinstance(starter, str) and not (ROOT / starter / "src").is_dir():
            errors.append(f"B00: starter must contain src/: {starter}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    print(
        f"Validated {len(manifest['projects'])} projects and B00 foundation "
        f"from {MANIFEST_PATH.relative_to(ROOT)}"
    )
    foundation = manifest["foundation"]
    print(f"PASS {foundation['id']} {foundation['level']}: {foundation['title']}")
    for project in sorted(manifest["projects"], key=lambda item: item["id"]):
        print(f"PASS {project['id']} {project['level']}: {project['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
