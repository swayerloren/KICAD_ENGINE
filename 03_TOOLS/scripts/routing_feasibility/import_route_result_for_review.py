from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage FreeRouting SES output for review only.")
    parser.add_argument("--ses", type=Path, required=True, help="Path to the SES file to stage.")
    parser.add_argument("--destination-dir", type=Path, required=True, help="Directory for the review bundle.")
    parser.add_argument("--run-manifest", type=Path, help="Optional run manifest to copy alongside the SES.")
    parser.add_argument("--project", help="Optional project name.")
    parser.add_argument("--variant-id", help="Optional variant ID.")
    return parser.parse_args()


def copy_optional(src: Path | None, destination_dir: Path) -> str | None:
    if src is None:
        return None
    resolved = src.resolve()
    if not resolved.exists():
        raise SystemExit(f"Optional file not found: {resolved}")
    target = destination_dir / resolved.name
    shutil.copy2(resolved, target)
    return str(target)


def main() -> int:
    args = parse_args()
    ses_path = args.ses.resolve()
    if not ses_path.exists():
        raise SystemExit(f"SES file not found: {ses_path}")

    destination_dir = args.destination_dir.resolve()
    destination_dir.mkdir(parents=True, exist_ok=True)
    staged_ses = destination_dir / ses_path.name
    shutil.copy2(ses_path, staged_ses)
    staged_manifest = copy_optional(args.run_manifest, destination_dir)

    review_note = destination_dir / "REVIEW_ONLY_IMPORT_NOTE.md"
    review_note.write_text(
        "\n".join(
            [
                "# Review-Only FreeRouting Bundle",
                "",
                "Status: `REVIEW_ONLY`",
                "",
                "This bundle stages FreeRouting output for inspection only.",
                "",
                "- Do not treat this SES as approved final routing.",
                "- Do not import this result into the canonical board by default.",
                "- Import, if any, belongs only in a copied workspace after backup and explicit approval.",
                "- USB, RF, switching-regulator, and high-current routing still require human engineering review.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    manifest: dict[str, Any] = {
        "tool": "import_route_result_for_review",
        "project": args.project,
        "variant_id": args.variant_id,
        "review_status": "REVIEW_ONLY",
        "ses_source": str(ses_path),
        "ses_staged": str(staged_ses),
        "run_manifest_staged": staged_manifest,
        "review_note": str(review_note),
        "notes": [
            "No KiCad PCB file was modified.",
            "This bundle is for human comparison and sandbox scoring support only.",
        ],
    }
    bundle_manifest = destination_dir / "review_bundle_manifest.json"
    bundle_manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
