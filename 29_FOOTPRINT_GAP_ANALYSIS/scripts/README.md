# Footprint Gap Analysis Scripts

Status: read-only installed-KiCad inventory and component-database candidate matching scripts.

## Scripts

| Script | Purpose |
| --- | --- |
| `inventory_kicad_footprints.py` | Index installed KiCad footprint libraries and summarize high-risk candidate categories. |
| `inventory_kicad_symbols.py` | Index installed KiCad symbol libraries and summarize common symbol candidate hits. |
| `match_component_db_to_footprints.py` | Compare `08_COMPONENT_DATABASE` JSON records to installed KiCad footprint candidates. |
| `create_missing_footprint_backlog.py` | Build missing-footprint, high-risk, connector, MCU/module, power, backlog, and summary reports. |

## Safety

- Scripts must not modify installed KiCad files.
- Scripts must not modify user global KiCad library tables.
- Scripts write only repo-local reports and generated indexes.
- Candidate matches are never footprint approvals.

## Typical Run Order

```powershell
python "29_FOOTPRINT_GAP_ANALYSIS\scripts\inventory_kicad_footprints.py" --kicad-root "C:\Program Files\KiCad\9.0" --version 9.0
python "29_FOOTPRINT_GAP_ANALYSIS\scripts\inventory_kicad_symbols.py" --kicad-root "C:\Program Files\KiCad\9.0" --version 9.0
python "29_FOOTPRINT_GAP_ANALYSIS\scripts\match_component_db_to_footprints.py" --kicad-root "C:\Program Files\KiCad\9.0" --version 9.0 --component-root "08_COMPONENT_DATABASE"
python "29_FOOTPRINT_GAP_ANALYSIS\scripts\create_missing_footprint_backlog.py"
```

## Verification Rule

Every generated candidate remains `UNVERIFIED` until checked against exact manufacturer package drawings, connector drawings, pad numbering, orientation, courtyard, paste/mask, and human review for high-risk categories.

