import argparse
import sys
from pathlib import Path


WARNINGS = [
    "WARN: connector orientation, polarity, pin 1, and rotation review is still required",
    "WARN: folder validation does not prove DRC, Gerber correctness, assembly approval, or upload readiness",
]


def required_paths(root, house):
    common_review = [
        root / "review" / "gerber_screenshots",
        root / "review" / "3d_screenshots",
        root / "review" / "orientation_checks.md",
    ]
    if house in {"all", "jlcpcb"}:
        for relative in ["jlcpcb/gerbers.zip", "jlcpcb/BOM_JLCPCB.csv", "jlcpcb/CPL_JLCPCB.csv", "jlcpcb/Assembly_Notes.md"]:
            yield root / relative
    if house in {"all", "pcbway"}:
        for relative in ["pcbway/gerbers.zip", "pcbway/BOM_PCBWay.csv", "pcbway/Centroid_PCBWay.csv", "pcbway/Assembly_Notes.md"]:
            yield root / relative
    for path in common_review:
        yield path


def main():
    parser = argparse.ArgumentParser(
        description="Validate NOT_FINAL PCBA package folder structure. Never edits KiCad files and never uploads anything."
    )
    parser.add_argument("--root", required=True, help="Revision folder such as manufacturing/rev_A")
    parser.add_argument("--house", choices=["all", "jlcpcb", "pcbway"], default="all")
    args = parser.parse_args()

    root = Path(args.root)
    errors = []
    if not root.exists():
        errors.append(f"root folder does not exist: {root}")
    else:
        for path in required_paths(root, args.house):
            if not path.exists():
                errors.append(f"missing required path: {path}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        for warning in WARNINGS:
            print(warning)
        return 1

    for warning in WARNINGS:
        print(warning)
    print("PASS: package folder structure exists")
    return 0


if __name__ == "__main__":
    sys.exit(main())

