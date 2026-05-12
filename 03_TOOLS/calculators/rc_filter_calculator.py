#!/usr/bin/env python3
"""Solve one value for a first-order RC filter."""

from __future__ import annotations

import argparse
import json
import math


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="First-order RC filter calculator.")
    parser.add_argument("--r-ohms", type=float, help="Resistance in ohms.")
    parser.add_argument("--c-farads", type=float, help="Capacitance in farads.")
    parser.add_argument("--fc-hz", type=float, help="Cutoff frequency in hertz.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    values = [args.r_ohms is not None, args.c_farads is not None, args.fc_hz is not None]
    if sum(values) != 2:
        raise SystemExit("Provide exactly two of --r-ohms, --c-farads, or --fc-hz.")

    if args.r_ohms is not None and args.c_farads is not None:
        fc = 1.0 / (2.0 * math.pi * args.r_ohms * args.c_farads)
        r = args.r_ohms
        c = args.c_farads
    elif args.r_ohms is not None and args.fc_hz is not None:
        r = args.r_ohms
        fc = args.fc_hz
        c = 1.0 / (2.0 * math.pi * r * fc)
    else:
        c = args.c_farads
        fc = args.fc_hz
        r = 1.0 / (2.0 * math.pi * c * fc)

    result = {
        "status": "AID_ONLY_NOT_PROOF",
        "formula": "fc = 1 / (2 * pi * R * C)",
        "inputs": {
            "r_ohms": args.r_ohms,
            "c_farads": args.c_farads,
            "fc_hz": args.fc_hz,
        },
        "outputs": {
            "r_ohms": r,
            "c_farads": c,
            "fc_hz": fc,
        },
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

