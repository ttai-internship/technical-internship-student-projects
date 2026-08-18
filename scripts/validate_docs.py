"""Validate local Markdown links and student Notebook schema details."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urldefrag, urlparse

import nbformat

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CELL_ID_PATTERN = re.compile(r"^[A-Za-z0-9-_]{1,64}$")
TEMPLATE_CONTRACTS = {
    "templates/internship-experience.md": ("## 任务记录", "## 节点记录", "## 证据边界"),
    "templates/student-submission.md": ("## 项目提交证据", "## 给导师的复盘", "### 学员收获", "### 建议", "### 推荐"),
}


def local_link_errors() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "artifacts"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith("#"):
                continue
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("//"):
                continue
            target_path, _ = urldefrag(target)
            candidate = (path.parent / target_path).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link: {target}")
    return errors


def notebook_errors() -> list[str]:
    errors: list[str] = []
    notebook_roots = [ROOT / "notebooks" / "student"]
    mentor_root = ROOT / "notebooks" / "mentor"
    if mentor_root.is_dir():
        notebook_roots.append(mentor_root)
    for notebook_root in notebook_roots:
        for path in notebook_root.rglob("*.ipynb"):
            try:
                notebook = nbformat.read(path, as_version=4)
            except Exception as error:  # noqa: BLE001
                errors.append(f"{path.relative_to(ROOT)}: invalid notebook: {error}")
                continue
            for index, cell in enumerate(notebook.cells, start=1):
                cell_id = cell.get("id")
                if not isinstance(cell_id, str) or not CELL_ID_PATTERN.fullmatch(cell_id):
                    errors.append(f"{path.relative_to(ROOT)}: cell {index} has invalid id {cell_id!r}")
    return errors


def template_contract_errors() -> list[str]:
    errors: list[str] = []
    for relative, headings in TEMPLATE_CONTRACTS.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing public template: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if re.search(rf"(?m)^{re.escape(heading)}\s*$", text) is None:
                errors.append(f"{relative}: missing required heading {heading}")
    return errors


def main() -> int:
    errors = local_link_errors() + notebook_errors() + template_contract_errors()
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    print("Documentation links and teaching Notebook IDs are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
