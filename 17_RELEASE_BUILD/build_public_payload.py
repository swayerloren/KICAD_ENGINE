#!/usr/bin/env python3
"""Dry-run-first public payload builder for KiCad Engine."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


BUILDER_VERSION = "0.1.0"

ROOT_ALLOW_FILES = {
    "AGENTS.md",
    "README.md",
    "README_GPT.md",
    "START_HERE_FOR_USERS.md",
    "START_HERE_FOR_AI_AGENTS.md",
    "QUICKSTART_WINDOWS.md",
    "QUICKSTART_MACOS.md",
    "QUICKSTART_LINUX.md",
    "INSTALLER_USER_GUIDE.md",
    "USER_MANUAL.md",
    "FAQ.md",
    "TROUBLESHOOTING.md",
    "LICENSE",
    "DISCLAIMER.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "PUBLIC_RELEASE_CHECKLIST.md",
    "health_check.py",
    "health_check.ps1",
    "HEALTH_CHECK_REPORT_TEMPLATE.md",
}

SANITIZATION_REQUIRED_FILES = {"FOR CHAT GPT.MD"}

ALLOW_DIRS = (
    ".vscode",
    ".prompts",
    "00_CODEX_START",
    "03_TOOLS/scripts",
    "03_TOOLS/kicad_app_intelligence",
    "03_TOOLS/kicad_library_intelligence",
    "06_DATASHEETS",
    "08_COMPONENT_DATABASE",
    "09_ACCURACY_ENGINE",
    "10_KNOWLEDGE_BASE",
    "11_LIBRARY_FACTORY",
    "12_REFERENCE_DESIGN_LIBRARY",
    "13_PART_INGESTION",
    "14_LAYOUT_AUTOMATION",
    "15_BENCHMARKS",
    "17_RELEASE_BUILD",
    "18_PUBLIC_DOCS",
    "21_LICENSE_ATTRIBUTION",
    "22_SECURITY",
    "26_AGENT_QUALITY",
    "28_SUPPLIER_INGESTION",
    "29_FOOTPRINT_GAP_ANALYSIS",
    "30_SUPPLIER_FOOTPRINT_MATCHES",
    "31_PLAYWRIGHT_RESEARCH_PIPELINE",
    "setup",
)

OPEN_SAMPLE_POLICY_DIRS = (
    "32_OPEN_KICAD_SAMPLE_INTAKE/candidates",
    "32_OPEN_KICAD_SAMPLE_INTAKE/attribution",
    "32_OPEN_KICAD_SAMPLE_INTAKE/templates",
    "32_OPEN_KICAD_SAMPLE_INTAKE/scripts",
)

OPEN_SAMPLE_POLICY_FILES = {
    "32_OPEN_KICAD_SAMPLE_INTAKE/README.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/INDEX.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/SOURCE_SELECTION_RULES.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/LICENSE_SCREENING_RULES.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_PROJECT_SCHEMA.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_IMPORT_WORKFLOW.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_REVIEW_WORKFLOW.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_PROMOTION_RULES.md",
    "32_OPEN_KICAD_SAMPLE_INTAKE/DO_NOT_IMPORT_LIST.md",
}

SAMPLE_ROOT = "19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board"
SAMPLE_DOC_FILES = {
    f"{SAMPLE_ROOT}/KICAD_ENGINE_SAMPLE_README.md",
    f"{SAMPLE_ROOT}/ORIGINAL_SOURCE_ATTRIBUTION.md",
    f"{SAMPLE_ROOT}/GOLDEN_PATH_DEMO_STATUS.md",
    f"{SAMPLE_ROOT}/LICENSE",
}
SAMPLE_REPORT_GLOB = f"{SAMPLE_ROOT}/reports/*.md"

TEST_PROJECT_PUBLIC_FILES = {
    "19_TEST_PROJECTS/README.md",
    "19_TEST_PROJECTS/INDEX.md",
    "19_TEST_PROJECTS/SAMPLE_PROJECTS_INDEX.md",
    "19_TEST_PROJECTS/HOW_TO_RUN_SAMPLE_PROJECTS.md",
    "19_TEST_PROJECTS/HOW_TO_INTERPRET_GATE_RESULTS.md",
}

PRUNE_DIR_NAMES = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules", ".venv", "venv"}

PRUNE_PREFIXES = (
    "02_HISTORY",
    "03_TOOLS/repos",
    "03_TOOLS/python_envs",
    "03_TOOLS/node_envs",
    "03_TOOLS/tool_logs",
    "03_TOOLS/windows/repos",
    "03_TOOLS/windows/logs",
    "03_TOOLS/linux/repos",
    "03_TOOLS/linux/logs",
    "05_OUTPUTS",
    "32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals",
    "32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples",
    "32_OPEN_KICAD_SAMPLE_INTAKE/benchmark_candidates",
    "99_BACKUPS",
    "installer/build",
    "installer/dist",
    "installer/node_modules",
    "installer/payload/repo-template",
    "17_RELEASE_BUILD/build",
    "17_RELEASE_BUILD/dist",
)

EXCLUDE_PREFIXES = PRUNE_PREFIXES + (
    f"{SAMPLE_ROOT}/custom_footprints",
    f"{SAMPLE_ROOT}/_verification",
    f"{SAMPLE_ROOT}/.gate_runs",
    f"{SAMPLE_ROOT}/fabrication",
)

EXCLUDE_SUFFIXES = {
    ".pdf",
    ".gbr",
    ".drl",
    ".xln",
    ".pos",
    ".zip",
    ".7z",
    ".rar",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".stl",
    ".step",
    ".stp",
    ".wrl",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
}

SAMPLE_SOURCE_SUFFIXES = {".kicad_pro", ".kicad_sch", ".kicad_pcb", ".kicad_mod", ".kicad_sym"}
SECRET_PATH_PATTERNS = ("*.key", "*.token", ".env", "secrets.*", "api_keys.*", "local_credentials.*", "private_config.*")
SECRET_ASSIGNMENT_RE = re.compile(r"(?i)\b(api[_-]?key|token|secret|password|private[_-]?key)\b\s*[:=]\s*[\"']?([A-Za-z0-9_./+=:-]{16,})")
PLACEHOLDER_TOKENS = ("example", "placeholder", "changeme", "change_me", "your_key", "your_token", "not_a_secret", "dummy", "xxxx")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def normalize_rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_under(rel: str, prefix: str) -> bool:
    clean = prefix.rstrip("/")
    return rel == clean or rel.startswith(clean + "/")


def is_sample_source(rel: str) -> bool:
    return is_under(rel, SAMPLE_ROOT) and (Path(rel).suffix.lower() in SAMPLE_SOURCE_SUFFIXES or rel.endswith("/fp-lib-table"))


def is_allowed_candidate(rel: str) -> tuple[bool, str]:
    if rel in ROOT_ALLOW_FILES:
        return True, "root public allowlist"
    if rel in SANITIZATION_REQUIRED_FILES:
        return False, "requires sanitized handoff copy before public payload"
    if rel in TEST_PROJECT_PUBLIC_FILES:
        return True, "public test-project documentation"
    if rel in SAMPLE_DOC_FILES or fnmatch.fnmatch(rel, SAMPLE_REPORT_GLOB):
        return True, "controlled sample markdown/license evidence only"
    if rel in OPEN_SAMPLE_POLICY_FILES:
        return True, "open sample intake policy file"
    if any(is_under(rel, prefix) for prefix in OPEN_SAMPLE_POLICY_DIRS):
        return True, "open sample intake metadata/template/script file"
    if any(is_under(rel, prefix) for prefix in ALLOW_DIRS):
        return True, "allowlisted public subsystem"
    return False, "not in public payload allowlist"


def path_secret_reason(rel: str) -> str | None:
    name = Path(rel).name
    for pattern in SECRET_PATH_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return f"secret-like filename pattern: {pattern}"
    return None


def content_secret_reason(path: Path) -> str | None:
    if path.stat().st_size > 1_000_000:
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return "could not read file for secret scan"
    for match in SECRET_ASSIGNMENT_RE.finditer(text):
        value = match.group(2).strip().strip("\"'").lower()
        if value.startswith("<") or value.startswith("${"):
            continue
        if any(token in value for token in PLACEHOLDER_TOKENS):
            continue
        return f"possible secret assignment for {match.group(1)}"
    return None


def exclusion_reason(rel: str, path: Path, max_bytes: int) -> str | None:
    if any(is_under(rel, prefix) for prefix in EXCLUDE_PREFIXES):
        return "excluded path per release exclusion rules"
    if is_sample_source(rel):
        return "sample KiCad source blocked until PUBLIC_BUNDLE_ALLOWED"
    if "FAB_READY" in rel.upper():
        return "FAB_READY marker is forbidden in public payload"
    secret_reason = path_secret_reason(rel)
    if secret_reason:
        return secret_reason
    suffix = path.suffix.lower()
    if suffix in EXCLUDE_SUFFIXES:
        return f"excluded file type: {suffix}"
    if path.stat().st_size > max_bytes:
        return f"file exceeds size limit ({path.stat().st_size} bytes > {max_bytes} bytes)"
    content_reason = content_secret_reason(path)
    if content_reason:
        return content_reason
    return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_repo_files(root: Path, output_root: Path) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    pruned: list[str] = []
    root = root.resolve()
    output_root = output_root.resolve()
    for current, dirs, names in os.walk(root):
        current_path = Path(current)
        kept_dirs = []
        for dirname in dirs:
            candidate = current_path / dirname
            rel_dir = normalize_rel(candidate, root)
            candidate_resolved = candidate.resolve()
            if candidate_resolved == output_root or output_root.is_relative_to(candidate_resolved):
                pruned.append(rel_dir + "/")
                continue
            if dirname in PRUNE_DIR_NAMES or any(is_under(rel_dir, prefix) for prefix in PRUNE_PREFIXES):
                pruned.append(rel_dir + "/")
                continue
            kept_dirs.append(dirname)
        dirs[:] = kept_dirs
        for name in names:
            path = current_path / name
            if output_root in path.resolve().parents:
                continue
            files.append(path)
    return files, sorted(set(pruned))


def render_report(manifest: dict) -> str:
    included_examples = "\n".join(f"- `{entry['path']}` ({entry['size_bytes']} bytes)" for entry in manifest["included"][:40])
    excluded_examples = "\n".join(f"- `{entry['path']}` - {entry['reason']}" for entry in manifest["excluded"][:60])
    warnings = "\n".join(
        f"- `{entry['status']}`: {entry['message']} Count: {entry.get('count', 'n/a')}"
        for entry in manifest["warnings"]
    )
    return f"""# Public Payload Dry-Run Report

Generated UTC: `{manifest['generated_at_utc']}`

Builder: `{manifest['builder']}`

Builder version: `{manifest['builder_version']}`

Mode: `{manifest['mode']}`

Final classification: `{manifest['final_classification']}`

Public release status: `{manifest['public_release_status']}`

Sample payload decision: `{manifest['sample_payload_decision']}`

## Summary

| Metric | Value |
| --- | ---: |
| Included files | {manifest['included_count']} |
| Included bytes | {manifest['included_bytes']} |
| Excluded files | {manifest['excluded_count']} |
| Warning records | {len(manifest['warnings'])} |

## Warnings

{warnings if warnings else '- None.'}

## Included Examples

{included_examples if included_examples else '- None.'}

## Excluded Examples

{excluded_examples if excluded_examples else '- None.'}

## Release Judgment

This dry-run does not create a public release artifact and does not approve
public distribution. The repo remains blocked pending human release review,
sample public-bundle review, and the remaining ATtiny85 engineering gate
blockers.
"""


def build_manifest(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    output_base = Path(args.output_dir).resolve()
    stamp = args.timestamp or utc_stamp()
    report_dir = output_base / stamp
    max_bytes = int(args.max_file_size_mb * 1024 * 1024)
    report_dir.mkdir(parents=True, exist_ok=True)

    included: list[dict] = []
    excluded: list[dict] = []
    warnings: list[dict] = []
    files, pruned = iter_repo_files(repo_root, output_base)

    for path in sorted(files, key=lambda item: normalize_rel(item, repo_root).lower()):
        rel = normalize_rel(path, repo_root)
        allowed, allow_reason = is_allowed_candidate(rel)
        if not allowed:
            excluded.append({"path": rel, "reason": allow_reason})
            continue
        reason = exclusion_reason(rel, path, max_bytes)
        if reason:
            excluded.append({"path": rel, "reason": reason})
            continue
        included.append({"path": rel, "size_bytes": path.stat().st_size, "sha256": sha256_file(path), "allow_reason": allow_reason})

    sample_source_candidates = [
        entry["path"]
        for entry in excluded
        if is_under(entry["path"], SAMPLE_ROOT)
        and (Path(entry["path"]).suffix.lower() in SAMPLE_SOURCE_SUFFIXES or entry["path"].endswith("/fp-lib-table") or "/custom_footprints/" in entry["path"])
    ]
    if sample_source_candidates:
        warnings.append(
            {
                "status": "SAMPLE_SOURCE_EXCLUDED",
                "message": "Controlled sample source remains excluded until human public-bundle status is exactly PUBLIC_BUNDLE_ALLOWED.",
                "count": len(sample_source_candidates),
            }
        )
    if pruned:
        warnings.append(
            {
                "status": "PRUNED_EXCLUDED_ROOTS",
                "message": "Large or unsafe roots were pruned instead of scanned file-by-file.",
                "count": len(pruned),
                "examples": pruned[:25],
            }
        )

    manifest = {
        "builder": "17_RELEASE_BUILD/build_public_payload.py",
        "builder_version": BUILDER_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "apply" if args.apply else "dry_run",
        "repo_root_sanitized": "<repo-root>",
        "max_file_size_mb": args.max_file_size_mb,
        "final_classification": "DRY_RUN_PASS_WITH_WARNINGS" if not args.apply else "APPLY_COMPLETED",
        "public_release_status": "BLOCKED_PENDING_HUMAN_RELEASE_REVIEW",
        "sample_payload_decision": "LINK_ONLY_PLUS_DOCS",
        "included_count": len(included),
        "included_bytes": sum(item["size_bytes"] for item in included),
        "excluded_count": len(excluded),
        "warnings": warnings,
        "included": included,
        "excluded": excluded,
    }

    if args.apply:
        target = Path(args.payload_dir).resolve()
        if target.exists() and not args.overwrite_output:
            raise SystemExit(f"Payload directory exists; pass --overwrite-output to replace it: {target}")
        if target.exists():
            shutil.rmtree(target)
        for item in included:
            source = repo_root / item["path"]
            destination = target / item["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        manifest["payload_dir_sanitized"] = "<payload-dir>"

    manifest_path = report_dir / "PUBLIC_PAYLOAD_DRY_RUN_MANIFEST.json"
    report_path = report_dir / "PUBLIC_PAYLOAD_DRY_RUN_REPORT.md"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    report_path.write_text(render_report(manifest), encoding="utf-8")
    print(f"Report: {report_path}")
    print(f"Manifest: {manifest_path}")
    print(f"Included files: {len(included)}")
    print(f"Excluded files: {len(excluded)}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a dry-run public payload manifest.")
    parser.add_argument("--repo-root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--output-dir", default="05_OUTPUTS/release_readiness/public_payload_dry_runs", help="Directory for generated dry-run reports.")
    parser.add_argument("--timestamp", default="", help="Optional fixed output timestamp.")
    parser.add_argument("--max-file-size-mb", type=float, default=5.0, help="Per-file size limit.")
    parser.add_argument("--apply", action="store_true", help="Copy included files to --payload-dir.")
    parser.add_argument("--payload-dir", default="05_OUTPUTS/release_readiness/public_payload_candidate", help="Apply-mode payload copy target.")
    parser.add_argument("--overwrite-output", action="store_true", help="Allow apply mode to replace an existing payload directory.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    return build_manifest(args)


if __name__ == "__main__":
    raise SystemExit(main())
