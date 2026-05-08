"""Read-only file audit for imported or normalized KiCad samples."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent


PATTERNS = {
    "kicad_pro": "*.kicad_pro",
    "kicad_sch": "*.kicad_sch",
    "kicad_pcb": "*.kicad_pcb",
    "kicad_sym": "*.kicad_sym",
    "kicad_mod": "*.kicad_mod",
    "gerber_like": "*.gbr",
    "drill": "*.drl",
    "pick_and_place": "*.pos",
    "pdf": "*.pdf",
    "step": "*.step",
}


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def inventory(path: Path) -> dict[str, object]:
    counts: dict[str, int] = {}
    examples: dict[str, list[str]] = {}
    for name, pattern in PATTERNS.items():
        files = sorted(path.rglob(pattern))
        counts[name] = len(files)
        examples[name] = [str(item.relative_to(path)) for item in files[:20]]
    license_files = [
        item
        for item in path.rglob("*")
        if item.is_file() and item.name.lower() in {"license", "license.md", "license.txt", "copying", "copying.txt"}
    ]
    return {
        "counts": counts,
        "examples": examples,
        "license_files": [str(item.relative_to(path)) for item in license_files[:20]],
        "has_kicad_source": any(counts[key] > 0 for key in ("kicad_pro", "kicad_sch", "kicad_pcb")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit sample project files read-only.")
    parser.add_argument("--sample-path", type=Path, required=True)
    parser.add_argument("--sample-id", default="sample")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "review_reports")
    args = parser.parse_args()

    sample_path = args.sample_path.resolve()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    run_id = timestamp()
    errors: list[str] = []
    if not sample_path.exists() or not sample_path.is_dir():
        errors.append("sample_path must be an existing folder.")
        data = {"counts": {}, "examples": {}, "license_files": [], "has_kicad_source": False}
    else:
        data = inventory(sample_path)

    status = "FILE_AUDIT_PASS" if data["has_kicad_source"] and not errors else "FILE_AUDIT_FAIL"
    report = {
        "status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sample_id": args.sample_id,
        "sample_path": str(sample_path),
        "errors": errors,
        **data,
        "public_bundle_status": "EXCLUDED_BY_DEFAULT",
        "human_review_required": True,
    }
    json_path = args.out_dir / f"file_audit_{args.sample_id}_{run_id}.json"
    md_path = args.out_dir / f"file_audit_{args.sample_id}_{run_id}.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Sample File Audit",
        "",
        f"Status: `{status}`",
        f"Sample path: `{sample_path}`",
        "",
        "| File Type | Count |",
        "| --- | ---: |",
    ]
    for key, count in report["counts"].items():
        lines.append(f"| `{key}` | {count} |")
    lines.extend(
        [
            "",
            f"License files found: `{len(report['license_files'])}`",
            "",
            "This audit is file presence evidence only. It does not verify electrical correctness, license compatibility, or fabrication readiness.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote file audit: {md_path}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
