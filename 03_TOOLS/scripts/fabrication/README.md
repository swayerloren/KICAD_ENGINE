# Fabrication Validators

Status: `ACTIVE_TOOLS`

These scripts validate CSV structure and NOT_FINAL PCBA package folder structure for JLCPCB, PCBWay, and universal internal review files.

They never edit KiCad files, never upload anything, and never prove assembly orientation. A `PASS` or `WARN` from these scripts only means the checked file/folder passed structural checks.

## Commands

```powershell
python 03_TOOLS\scripts\fabrication\validate_jlcpcb_bom.py 17_RELEASE_BUILD\templates\BOM_JLCPCB_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_jlcpcb_cpl.py 17_RELEASE_BUILD\templates\CPL_JLCPCB_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_pcbway_bom.py 17_RELEASE_BUILD\templates\BOM_PCBWay_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_pcbway_centroid.py 17_RELEASE_BUILD\templates\Centroid_PCBWay_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_universal_bom.py 17_RELEASE_BUILD\templates\BOM_UNIVERSAL_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_universal_pick_and_place.py 17_RELEASE_BUILD\templates\PickAndPlace_UNIVERSAL_TEMPLATE.csv
python 03_TOOLS\scripts\fabrication\validate_pcba_package_folder.py --root manufacturing\rev_A
```

## Result Meanings

- `PASS`: structural checks passed.
- `WARN`: structural checks passed, but human/proof review is still required or optional package evidence is missing.
- `FAIL`: required structure or field checks failed.

