"""Validate one generated student assignment without mentor-only material."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / ".internship" / "assignment.json"
BASELINE_PATH = ROOT / ".internship" / "baseline-manifest.json"
PUBLIC_REPOSITORY = "ttai-internship/technical-internship-student-projects"
PROJECT_LEVELS = {
    "B00": "foundation",
    "B01": "beginner",
    "B02": "beginner",
    "B03": "beginner",
    "M01": "intermediate",
    "M02": "intermediate",
    "M03": "intermediate",
    "A01": "advanced",
    "A02": "advanced",
    "A03": "advanced",
}
DURATION_DAYS = {"one-week": 7, "one-month": 30, "two-month": 60, "half-year": 180}
REQUIRED_FILES = {
    "AI_USE.md",
    "ASSIGNMENT.md",
    "ASSIGNMENT_SCOPE.md",
    "SUBMISSION.md",
    "notebook.ipynb",
    "pyproject.toml",
    "uv.lock",
}
REQUIRED_METADATA = {
    "schema_version",
    "assignment_id",
    "project_id",
    "level",
    "duration",
    "assignment_mode",
    "public_materials_repository",
    "public_materials_revision",
    "status",
    "created_at",
    "due_at",
    "retention_days_after_acceptance",
    "accepted_at",
    "delete_after",
    "core_required",
    "final_score_requires_manual_review",
    "paper_pack_id",
}
ALLOWED_STATUSES = {"assigned", "in_progress", "submitted", "accepted", "deleted"}
FORBIDDEN_PARTS = {"mentor", "hidden-tests", "hidden_tests", "solutions", "answer"}
SKIPPED_DIRECTORIES = {".git", ".venv", ".pytest_cache", ".mypy_cache", ".ruff_cache", "__pycache__"}
PROTECTED_PREFIXES = (".github/", "scripts/")
PROTECTED_FILES = {
    "ASSIGNMENT.md",
    "ASSIGNMENT_SCOPE.md",
    "pyproject.toml",
    "requirements.txt",
    "uv.lock",
}
REQUIRED_PROTECTED_FILES = {
    ".github/workflows/student-checks.yml",
    "ASSIGNMENT.md",
    "ASSIGNMENT_SCOPE.md",
    "pyproject.toml",
    "scripts/security_scan.py",
    "scripts/validate_submission.py",
    "uv.lock",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_iso_date(value: Any, field: str, errors: list[str]) -> date | None:
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        errors.append(f"{field} must be an ISO date")
        return None


def load_metadata() -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    try:
        raw = METADATA_PATH.read_bytes()
    except OSError as error:
        return None, [f"cannot read {METADATA_PATH.relative_to(ROOT)}: {error}"]
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("assignment.json must be UTF-8 without BOM")
    try:
        metadata = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, [*errors, f"invalid assignment.json: {error}"]
    if not isinstance(metadata, dict):
        return None, [*errors, "assignment.json must contain an object"]
    return metadata, errors


def metadata_errors() -> list[str]:
    metadata, errors = load_metadata()
    if metadata is None:
        return errors
    missing = REQUIRED_METADATA - metadata.keys()
    if missing:
        errors.append(f"assignment.json missing fields: {sorted(missing)}")
    if metadata.get("schema_version") != 3:
        errors.append("assignment.json schema_version must be 3")

    assignment_id = str(metadata.get("assignment_id", ""))
    if re.fullmatch(r"[A-Za-z0-9._-]+", assignment_id) is None:
        errors.append("assignment_id must be pseudonymous and filename-safe")
    github_repository = os.environ.get("GITHUB_REPOSITORY")
    if github_repository and github_repository.startswith("ttai-internship/"):
        repository_name = github_repository.partition("/")[2]
        if repository_name != assignment_id:
            errors.append("GitHub repository name must exactly match assignment_id")

    project = str(metadata.get("project_id", ""))
    if project not in PROJECT_LEVELS:
        errors.append(f"unsupported project_id: {project!r}")
    elif metadata.get("level") != PROJECT_LEVELS[project]:
        errors.append(f"level must be {PROJECT_LEVELS[project]!r} for {project}")
    duration = str(metadata.get("duration", ""))
    if duration not in DURATION_DAYS:
        errors.append(f"unsupported duration: {duration!r}")
    elif project == "B00" and duration != "one-week":
        errors.append("B00 is assignable only for one-week")

    expected_mode = "requires-paper-pack" if project == "A03" else "direct"
    if metadata.get("assignment_mode") != expected_mode:
        errors.append(f"assignment_mode must be {expected_mode!r} for {project or 'this project'}")
    paper_pack = metadata.get("paper_pack_id")
    if project == "A03" and (not isinstance(paper_pack, str) or not paper_pack.strip()):
        errors.append("A03 requires a non-empty paper_pack_id")
    elif project != "A03" and paper_pack is not None:
        errors.append("paper_pack_id must be null outside A03")

    if metadata.get("public_materials_repository") != PUBLIC_REPOSITORY:
        errors.append("public_materials_repository must point to the public student repository")
    if re.fullmatch(r"[0-9a-f]{40}", str(metadata.get("public_materials_revision", ""))) is None:
        errors.append("public_materials_revision must be a full Git commit SHA")
    status = metadata.get("status")
    if status not in ALLOWED_STATUSES:
        errors.append(f"invalid assignment status: {status!r}")
    if metadata.get("retention_days_after_acceptance") != 30:
        errors.append("retention_days_after_acceptance must be 30")
    if metadata.get("core_required") is not True:
        errors.append("core_required must remain true")
    if metadata.get("final_score_requires_manual_review") is not True:
        errors.append("final_score_requires_manual_review must remain true")

    created_at = parse_iso_date(metadata.get("created_at"), "created_at", errors)
    due_at = parse_iso_date(metadata.get("due_at"), "due_at", errors)
    if created_at and due_at and duration in DURATION_DAYS:
        expected_due = created_at + timedelta(days=DURATION_DAYS[duration])
        if due_at != expected_due:
            errors.append(f"due_at must be {expected_due.isoformat()} for {duration}")

    accepted_raw = metadata.get("accepted_at")
    delete_raw = metadata.get("delete_after")
    if status in {"assigned", "in_progress", "submitted"}:
        if accepted_raw is not None or delete_raw is not None:
            errors.append(f"accepted_at and delete_after must be null while status is {status!r}")
    elif status in {"accepted", "deleted"}:
        accepted_at = parse_iso_date(accepted_raw, "accepted_at", errors)
        delete_after = parse_iso_date(delete_raw, "delete_after", errors)
        if accepted_at and created_at and accepted_at < created_at:
            errors.append("accepted_at cannot be earlier than created_at")
        if accepted_at and delete_after and delete_after < accepted_at + timedelta(days=30):
            errors.append("delete_after must preserve at least 30 days after acceptance")
    return errors


def assignment_paths() -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    symbolic: list[str] = []
    for directory, child_directories, names in os.walk(ROOT, followlinks=False):
        base = Path(directory)
        retained: list[str] = []
        for name in child_directories:
            path = base / name
            relative = path.relative_to(ROOT).as_posix()
            if is_symbolic_path(path):
                symbolic.append(relative)
            elif name not in SKIPPED_DIRECTORIES and not name.startswith(".venv"):
                retained.append(name)
        child_directories[:] = retained
        for name in names:
            path = base / name
            if is_symbolic_path(path):
                symbolic.append(path.relative_to(ROOT).as_posix())
            else:
                files.append(path)
    return files, sorted(symbolic)


def is_symbolic_path(path: Path) -> bool:
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())


def structure_errors() -> list[str]:
    errors = [f"missing required file: {name}" for name in sorted(REQUIRED_FILES) if not (ROOT / name).is_file()]
    files, symbolic = assignment_paths()
    if symbolic:
        errors.append(f"symbolic links are not allowed in an assignment: {symbolic}")
    for path in files:
        relative = path.relative_to(ROOT)
        if FORBIDDEN_PARTS.intersection(part.casefold() for part in relative.parts):
            errors.append(f"mentor-only path is forbidden: {relative}")
    return errors


def safe_baseline_path(value: str) -> PurePosixPath:
    if "\\" in value:
        raise ValueError(f"baseline path must use forward slashes: {value!r}")
    relative = PurePosixPath(value)
    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise ValueError(f"unsafe baseline path: {value!r}")
    return relative


def protected_file_errors() -> list[str]:
    try:
        raw = BASELINE_PATH.read_bytes()
    except OSError as error:
        return [f"cannot read .internship/baseline-manifest.json: {error}"]
    errors: list[str] = []
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("baseline-manifest.json must be UTF-8 without BOM")
    try:
        document = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return [*errors, f"invalid baseline manifest: {error}"]
    if not isinstance(document, dict) or document.get("schema_version") != 2:
        return [*errors, "baseline manifest schema_version must be 2"]
    baseline = document.get("files")
    if not isinstance(baseline, dict):
        return [*errors, "baseline manifest files must be an object"]

    normalized: dict[str, str] = {}
    for raw_relative, expected_hash in baseline.items():
        if not isinstance(raw_relative, str) or not isinstance(expected_hash, str):
            errors.append("baseline file entries must be string pairs")
            continue
        try:
            relative = safe_baseline_path(raw_relative)
        except ValueError as error:
            errors.append(str(error))
            continue
        if re.fullmatch(r"[0-9a-f]{64}", expected_hash) is None:
            errors.append(f"invalid SHA-256 for baseline file: {raw_relative}")
            continue
        normalized[raw_relative] = expected_hash
        if raw_relative in PROTECTED_FILES or raw_relative.startswith(PROTECTED_PREFIXES):
            path = ROOT.joinpath(*relative.parts)
            if is_symbolic_path(path) or not path.is_file():
                errors.append(f"protected file was removed or replaced by a link: {raw_relative}")
            elif digest(path) != expected_hash:
                errors.append(f"protected file changed: {raw_relative}")
    missing_protected = REQUIRED_PROTECTED_FILES - normalized.keys()
    if missing_protected:
        errors.append(f"baseline is missing protected files: {sorted(missing_protected)}")
    return errors


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(rf"(?ms)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)")
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def meaningful_length(text: str) -> int:
    return len(re.sub(r"[\s#`|:_*\-]+", "", text))


def final_submission_errors() -> list[str]:
    errors: list[str] = []
    try:
        submission = (ROOT / "SUBMISSION.md").read_text(encoding="utf-8")
        ai_use = (ROOT / "AI_USE.md").read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        return [f"cannot read final submission documents: {error}"]

    if "在这里填写命令" in submission:
        errors.append("SUBMISSION.md still contains the run-command placeholder")
    required_sections = ("项目", "我完成的 Core 内容", "运行方法", "验证结果", "我学到的内容")
    incomplete = [heading for heading in required_sections if meaningful_length(section_body(submission, heading)) < 2]
    if incomplete or meaningful_length(submission) < 80:
        errors.append(f"SUBMISSION.md is incomplete; empty or too-short sections: {incomplete}")

    no_ai = re.search(r"(?m)^\s*无实质性 AI 使用[。.]?\s*$", ai_use) is not None
    if not no_ai:
        table_rows = []
        for line in ai_use.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if (
                len(cells) == 5
                and all(cells)
                and not all(set(cell) <= {"-", ":"} for cell in cells)
                and cells[0] != "工具"
            ):
                table_rows.append(cells)
        if not table_rows:
            errors.append("AI_USE.md must disclose a substantial AI use or state no substantial AI use")
        for label in ("建议摘要", "我的处理", "原因"):
            match = re.search(rf"(?m)^-\s*{label}：\s*(.+)$", ai_use)
            if match is None or meaningful_length(match.group(1)) < 2:
                errors.append(f"AI_USE.md must complete the {label!r} field")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final", action="store_true", help="also require completed submission evidence")
    args = parser.parse_args()
    structure = structure_errors()
    errors = metadata_errors() + structure + protected_file_errors()
    if args.final and not structure:
        errors.extend(final_submission_errors())
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    print("Assignment metadata, structure and protected files are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
