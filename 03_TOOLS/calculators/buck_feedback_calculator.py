#!/usr/bin/env python3
"""Solve one resistor in a standard buck feedback divider."""

from __future__ import annotations

import argparse
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Buck feedback divider calculator.")
    parser.add_argument("--vref", type=float, required=True, help="Feedback reference voltage.")
    parser.add_argument("--vout", type=float, required=True, help="Target output voltage.")
    parser.add_argument("--r-top-ohms", type=float, help="Known upper feedback resistor.")
    parser.add_argument("--r-bottom-ohms", type=float, help="Known lower feedback resistor.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if (args.r_top_ohms is None) == (args.r_bottom_ohms is None):
        raise SystemExit("Provide exactly one of --r-top-ohms or --r-bottom-ohms.")
    if args.vout <= args.vref:
        raise SystemExit("vout must be greater than vref for a boost-above-reference divider.")

    gain = (args.vout / args.vref) - 1
    if args.r_bottom_ohms is not None:
        r_bottom = args.r_bottom_ohms
        r_top = r_bottom * gain
    else:
        r_top = args.r_top_ohms
        r_bottom = r_top / gain

    result = {
        "status": "AID_ONLY_NOT_PROOF",
        "formula": "vout = vref * (1 + r_top / r_bottom)",
        "inputs": {
            "vref": args.vref,
            "vout": args.vout,
            "r_top_ohms": args.r_top_ohms,
            "r_bottom_ohms": args.r_bottom_ohms,
        },
        "outputs": {
            "r_top_ohms": r_top,
            "r_bottom_ohms": r_bottom,
        },
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

