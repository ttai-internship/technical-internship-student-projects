"""Validate every supported dependency entry point against one policy file."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "config" / "dependency_policy.json"


def _requirements(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def _environment_pip_dependencies(path: Path) -> list[str]:
    dependencies: list[str] = []
    in_pip = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "- pip:":
            in_pip = True
            continue
        if in_pip and line.startswith("      - "):
            dependencies.append(stripped.removeprefix("- ").strip('"\''))
        elif in_pip and stripped and not line.startswith("      "):
            in_pip = False
    return dependencies


def validate() -> list[str]:
    errors: list[str] = []
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    expected_root = policy["root"]
    actual_default = pyproject["project"].get("dependencies", [])
    if actual_default != expected_root["default"]:
        errors.append(f"pyproject default dependencies differ: {actual_default!r}")
    actual_groups = pyproject.get("dependency-groups", {})
    for group, expected in expected_root.items():
        if group == "default":
            continue
        if actual_groups.get(group) != expected:
            errors.append(f"pyproject group {group!r} differs: {actual_groups.get(group)!r}")
    unexpected_groups = set(actual_groups) - (set(expected_root) - {"default"})
    if unexpected_groups:
        errors.append(f"unexpected pyproject dependency groups: {sorted(unexpected_groups)}")

    actual_environment = _environment_pip_dependencies(ROOT / "environment.yml")
    if actual_environment != policy["environment"]:
        errors.append(f"environment.yml pip dependencies differ: {actual_environment!r}")

    project_ids = set(policy["assignment_dependencies"])
    expected_ids = {"B00", "B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03"}
    if project_ids != expected_ids:
        errors.append(f"assignment dependency IDs differ: {sorted(project_ids)}")

    for project_id, relative in policy["starter_requirement_files"].items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{project_id}: missing requirements file {relative}")
            continue
        actual = _requirements(path)
        expected = policy["assignment_dependencies"][project_id]
        if actual != expected:
            errors.append(f"{project_id}: requirements differ: {actual!r} != {expected!r}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    print("Dependency policy is consistent across pyproject, Conda and starter requirements.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
