import sys

from fabrication_validator_common import run_csv_validator


if __name__ == "__main__":
    sys.exit(
        run_csv_validator(
            "Validate JLCPCB BOM CSV structure. Does not edit KiCad files or upload anything.",
            ["Comment", "Designator", "Footprint", "LCSC Part #", "Quantity", "Manufacturer", "Manufacturer Part Number", "Notes"],
            ["Comment", "Designator", "Footprint"],
            quantity_column="Quantity",
            designator_column="Designator",
        )
    )
