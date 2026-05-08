import sys

from fabrication_validator_common import run_csv_validator


if __name__ == "__main__":
    sys.exit(
        run_csv_validator(
            "Validate universal pick-and-place CSV structure. Does not edit KiCad files or upload anything.",
            ["Designator", "Mid X", "Mid Y", "Layer", "Rotation"],
            ["Designator", "Mid X", "Mid Y", "Layer", "Rotation"],
            numeric_columns=["Mid X", "Mid Y", "Rotation"],
            layer_column="Layer",
        )
    )
