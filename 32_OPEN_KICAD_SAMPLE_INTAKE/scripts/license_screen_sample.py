"""Practical license screening for local sample folders.

This is not legal advice. It identifies common license files and assigns a
conservative status for human review.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


KNOWN_PUBLIC_LICENSE_HINTS = {
    "mit license": "MIT",
    "apache license": "Apache",
    "cern open hardware licence": "CERN-OHL",
    "cern-ohl": "CERN-OHL",
    "creative commons attribution": "CC-BY",
    "gnu general public license": "GPL",
    "gnu lesser general public license": "LGPL",
}

RESTRICTED_HINTS = ("all rights reserved", "proprietary", "confidential", "no redistribution")


def find_license_files(path: Path) -> list[Path]:
    names = {"license", "license.md", "license.txt", "copying", "copying.txt", "copyright"}
    return [item for item in path.rglob("*") if item.is_file() and item.name.lower() in names]


def screen_text(text: str) -> tuple[str, str]:
    lower = text.lower()
    for hint in RESTRICTED_HINTS:
        if hint in lower:
            return "PROPRIETARY_OR_RESTRICTED", "Restricted-language hint found."
    for hint, name in KNOWN_PUBLIC_LICENSE_HINTS.items():
        if hint in lower:
            return "NEEDS_HUMAN_LICENSE_REVIEW", f"Common public license hint found: {name}. Confirm hardware-file scope."
    return "NEEDS_HUMAN_LICENSE_REVIEW", "License file found but compatibility not classified."


def main() -> int:
    parser = argparse.ArgumentParser(description="Screen a sample folder for license evidence.")
    parser.add_argument("--sample-path", type=Path, required=True)
    parser.add_argument("--sample-id", default="sample")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "attribution")
    args = parser.parse_args()

    sample_path = args.sample_path.resolve()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    license_files = find_license_files(sample_path) if sample_path.exists() and sample_path.is_dir() else []
    if not license_files:
        status = "NO_LICENSE_FOUND"
        notes = "No common license file found."
        license_name = "UNKNOWN"
        excerpt = ""
    else:
        text = license_files[0].read_text(encoding="utf-8", errors="replace")
        status, notes = screen_text(text[:20000])
        license_name = "UNKNOWN"
        excerpt = " ".join(text.split())[:500]

    record = {
        "status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sample_id": args.sample_id,
        "sample_path": str(sample_path),
        "license_files": [str(item.relative_to(sample_path)) for item in license_files],
        "license_name": license_name,
        "notes": notes,
        "license_text_excerpt": excerpt,
        "public_bundle_status": "EXCLUDED_BY_DEFAULT" if status != "PUBLIC_BUNDLE_ALLOWED" else "PUBLIC_BUNDLE_ALLOWED",
        "human_license_review_required": True,
        "not_legal_advice": True,
    }
    safe_id = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in args.sample_id)
    json_path = args.out_dir / f"license_screen_{safe_id}.json"
    md_path = args.out_dir / f"license_screen_{safe_id}.md"
    json_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(
        "\n".join(
            [
                "# License Screen Record",
                "",
                f"Status: `{status}`",
                f"Sample: `{args.sample_id}`",
                f"Sample path: `{sample_path}`",
                f"License files found: `{len(license_files)}`",
                f"Notes: {notes}",
                "",
                "This is practical screening only, not legal advice. Human review is required before public bundling.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote license screen: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
