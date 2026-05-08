#!/usr/bin/env python3
"""Validate a local KiCad install using the portable discovery layer."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

from find_kicad import detect_kicad_environment


@dataclass
class ValidationRow:
    status: str
    name: str
    detail: str


def status_for(found: bool, *, required: bool = False) -> str:
    if found:
        return "PASS"
    return "FAIL" if required else "WARN"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-root", help="Optional KiCad install root override.")
    parser.add_argument("--kicad-cli", help="Optional kicad-cli override.")
    parser.add_argument("--kicad-exe", help="Optional kicad GUI executable override.")
    parser.add_argument("--require-kicad", action="store_true", help="Fail if KiCad is not detected.")
    parser.add_argument("--require-cli", action="store_true", help="Fail if kicad-cli is not detected.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text summary.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = detect_kicad_environment(
        explicit_root=args.kicad_root,
        explicit_cli=args.kicad_cli,
        explicit_gui=args.kicad_exe,
    )

    rows = [
        ValidationRow(
            status_for(payload["kicad_root"]["detected"], required=args.require_kicad),
            "KiCad root",
            payload["kicad_root"]["path"] or payload["missing_message"],
        ),
        ValidationRow(
            status_for(bool(payload["kicad_gui"]["path"]), required=args.require_kicad),
            "KiCad GUI",
            payload["kicad_gui"]["path"] or "KiCad GUI executable not detected.",
        ),
        ValidationRow(
            status_for(bool(payload["kicad_cli"]["path"]), required=args.require_cli or args.require_kicad),
            "kicad-cli",
            payload["kicad_cli"]["path"] or "kicad-cli not detected.",
        ),
        ValidationRow(
            "PASS" if payload["pcbnew"]["available"] else "WARN",
            "pcbnew",
            payload["pcbnew"]["message"],
        ),
    ]

    if args.json:
        print(json.dumps({"rows": [row.__dict__ for row in rows], "payload": payload}, indent=2))
    else:
        print("KiCad install validation")
        print(f"- Platform: `{payload['platform']}`")
        for row in rows:
            print(f"- {row.status}: `{row.name}` - {row.detail}")
        if payload["missing_message"]:
            print(f"- Guidance: {payload['missing_message']}")

    failed = any(row.status == "FAIL" for row in rows)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
