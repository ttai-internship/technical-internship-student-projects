"""Execute all teaching notebooks into ignored artifact copies."""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = ROOT / "notebooks"
OUTPUT_ROOT = ROOT / "artifacts" / "notebooks"
MANIFEST_PATH = ROOT / "config" / "projects.json"


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def execute(notebook_path: Path, project_root: Path) -> Path:
    with notebook_path.open(encoding="utf-8") as handle:
        notebook = nbformat.read(handle, as_version=4)
    source_path = str(project_root / "src")
    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = os.pathsep.join(
        value for value in (source_path, existing_pythonpath) if value
    )
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(notebook_path.parent)}, "env": env},
    )
    client.execute()
    output_path = OUTPUT_ROOT / notebook_path.relative_to(NOTEBOOK_ROOT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        nbformat.write(notebook, handle)
    return output_path


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    entries = list(manifest["projects"])
    if isinstance(manifest.get("foundation"), dict):
        entries.append(manifest["foundation"])
    notebooks = [
        (ROOT / entry["notebook"], ROOT / entry["starter"])
        for entry in entries
    ]
    if not notebooks:
        print("No notebooks found", file=sys.stderr)
        return 1
    failures = []
    for notebook_path, project_root in sorted(notebooks, key=lambda item: str(item[0])):
        try:
            if not notebook_path.is_file():
                raise FileNotFoundError(notebook_path)
            output_path = execute(notebook_path, project_root)
            print(f"PASS {notebook_path.relative_to(ROOT)} -> {output_path.relative_to(ROOT)}")
        except Exception as error:  # noqa: BLE001
            failures.append((notebook_path, error))
            print(f"FAIL {notebook_path.relative_to(ROOT)}: {error}", file=sys.stderr)
    if failures:
        return 1
    print(f"Executed {len(notebooks)} notebooks successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
