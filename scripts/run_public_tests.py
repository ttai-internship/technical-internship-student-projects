from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "projects.json"


def load_projects() -> list[dict[str, object]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return manifest["projects"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run public tests from the project manifest.")
    parser.add_argument("--project", help="Run only one project ID, such as B01.")
    args = parser.parse_args()

    projects = sorted(load_projects(), key=lambda project: str(project["id"]))
    if args.project:
        projects = [project for project in projects if project["id"] == args.project]
        if not projects:
            print(f"Unknown project: {args.project}", file=sys.stderr)
            return 2

    failed: list[str] = []
    for project_info in projects:
        project = ROOT / str(project_info["starter"])
        tests = ROOT / str(project_info["tests"])
        print(f"=== {project.relative_to(ROOT)} ===", flush=True)
        env = os.environ.copy()
        source_path = str(project / "src")
        existing_pythonpath = env.get("PYTHONPATH")
        env["PYTHONPATH"] = os.pathsep.join(
            value for value in (source_path, existing_pythonpath) if value
        )
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-v"],
            cwd=project,
            env=env,
            check=False,
        )
        if completed.returncode != 0:
            failed.append(str(project.relative_to(ROOT)))
    if failed:
        print("Failed projects:")
        print("\n".join(failed))
        return 1
    print(f"All {len(projects)} project test suites passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
