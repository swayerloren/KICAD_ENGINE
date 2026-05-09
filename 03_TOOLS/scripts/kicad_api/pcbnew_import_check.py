#!/usr/bin/env python3
"""Safe pcbnew import check for portable KiCad Engine workflows."""

from __future__ import annotations

import argparse
import json

from kicad_python_context import build_kicad_python_context


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-root", help="Optional KiCad install root override.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text summary.")
    parser.add_argument("--require-pcbnew", action="store_true", help="Return non-zero if no workable pcbnew context is available.")
    return parser.parse_args()


def summarize(payload: dict) -> dict:
    pcbnew = payload["pcbnew"]
    if pcbnew["current_python_available"]:
        status = "PASS"
    elif pcbnew["available"]:
        status = "WARN"
    else:
        status = "FAIL"
    return {
        "status": status,
        "pcbnew_available": pcbnew["available"],
        "current_python_available": pcbnew["current_python_available"],
        "discovered_path_available": pcbnew["discovered_path_available"],
        "kicad_python_available": pcbnew["kicad_python_available"],
        "recommended_context": pcbnew["recommended_context"],
        "message": pcbnew["message"],
        "guidance": pcbnew["guidance"],
        "context": payload,
    }


def main() -> int:
    args = parse_args()
    payload = build_kicad_python_context(explicit_root=args.kicad_root)
    summary = summarize(payload)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print("pcbnew import check")
        print(f"- Status: `{summary['status']}`")
        print(f"- Current Python available: `{summary['current_python_available']}`")
        print(f"- KiCad Python available: `{summary['kicad_python_available']}`")
        print(f"- Recommended context: `{summary['recommended_context']}`")
        print(f"- Detail: {summary['message']}")
        print("- Guidance:")
        for line in summary["guidance"]:
            print(f"  - {line}")

    if args.require_pcbnew and not summary["pcbnew_available"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
