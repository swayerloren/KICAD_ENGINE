#!/usr/bin/env python3
"""First-pass trace-width worksheet.

This is intentionally a stub, not an IPC-proof calculator. The user must
provide the current-density assumption and formula/source note.
"""

from __future__ import annotations

import argparse
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="First-pass trace-width worksheet.")
    parser.add_argument("--current-a", type=float, required=True, help="Target current in amps.")
    parser.add_argument(
        "--current-density-a-per-mm",
        type=float,
        required=True,
        help="Chosen current-density assumption in A/mm of trace width.",
    )
    parser.add_argument("--source-note", default="", help="Formula/source note for the assumption.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    width_mm = args.current_a / args.current_density_a_per_mm
    result = {
        "status": "AID_ONLY_NOT_PROOF",
        "formula": "width_mm = current_a / current_density_a_per_mm",
        "inputs": {
            "current_a": args.current_a,
            "current_density_a_per_mm": args.current_density_a_per_mm,
            "source_note": args.source_note,
        },
        "outputs": {
            "minimum_width_mm": width_mm,
            "minimum_width_mil": width_mm / 0.0254,
        },
        "required_followup": [
            "record board stackup and copper weight",
            "cross-check against fabricator capability",
            "cross-check against thermal-rise target",
        ],
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

