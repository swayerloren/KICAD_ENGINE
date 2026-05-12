#!/usr/bin/env python3
"""Solve one resistor in a standard voltage divider."""

from __future__ import annotations

import argparse
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Voltage divider calculator.")
    parser.add_argument("--vin", type=float, required=True, help="Input voltage.")
    parser.add_argument("--vout", type=float, required=True, help="Target output voltage.")
    parser.add_argument("--r-top-ohms", type=float, help="Known top resistor.")
    parser.add_argument("--r-bottom-ohms", type=float, help="Known bottom resistor.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if (args.r_top_ohms is None) == (args.r_bottom_ohms is None):
        raise SystemExit("Provide exactly one of --r-top-ohms or --r-bottom-ohms.")
    if args.vin <= args.vout:
        raise SystemExit("vin must be greater than vout for a passive divider.")

    ratio = args.vout / args.vin
    if args.r_bottom_ohms is not None:
        r_top = args.r_bottom_ohms * ((1 / ratio) - 1)
        r_bottom = args.r_bottom_ohms
    else:
        r_top = args.r_top_ohms
        r_bottom = r_top / ((1 / ratio) - 1)

    divider_current = args.vin / (r_top + r_bottom)
    result = {
        "status": "AID_ONLY_NOT_PROOF",
        "formula": "vout = vin * (r_bottom / (r_top + r_bottom))",
        "inputs": {
            "vin": args.vin,
            "vout": args.vout,
            "r_top_ohms": args.r_top_ohms,
            "r_bottom_ohms": args.r_bottom_ohms,
        },
        "outputs": {
            "r_top_ohms": r_top,
            "r_bottom_ohms": r_bottom,
            "divider_current_a": divider_current,
        },
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

