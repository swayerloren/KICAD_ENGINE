"""SCHEMATIC_ANNOTATION_GATE.

Aggregates the existing annotation report when present and falls back to a
read-only schematic reference scan when it is missing.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from .base_gate import FAIL, INCOMPLETE, PASS, BaseGate, GateBlocker


class SchematicAnnotationGate(BaseGate):
    gate_id = "SCHEMATIC_ANNOTATION_GATE"
    gate_name = "Schematic Annotation Gate"
    stage = 1

    def evaluate(self):
        schematic_files = self.find_project_files("*.kicad_sch")
        annotation_json = self.first_existing("reports/ANNOTATION_CHECK.json")
        annotation_md = self.first_existing("reports/ANNOTATION_CHECK.md")
        evidence = [
            self.evidence_path("schematic", schematic_files[0] if schematic_files else None),
            self.evidence_path("annotation_json", annotation_json),
            self.evidence_path("annotation_markdown", annotation_md),
        ]

        if not schematic_files:
            return self.make_result(
                INCOMPLETE,
                "No .kicad_sch file was found.",
                [self.missing_evidence_blocker("schematic file", "*.kicad_sch")],
                evidence=evidence,
            )

        if annotation_json and annotation_json.exists():
            data = json.loads(self.read_text(annotation_json))
            summary = data.get("summary", {})
            result = str(summary.get("result", "")).upper()
            counts = summary.get("counts", {})
            failing_checks = [
                check
                for check in data.get("checks", [])
                if str(check.get("status", "")).upper() == "FAIL"
            ]
            blockers = [
                GateBlocker(
                    id=str(check.get("code", "ANNOTATION_CHECK_FAILED")),
                    severity="CRITICAL",
                    message=(
                        f"{check.get('reference', '<project>')}: "
                        f"{check.get('message', 'Annotation check failed.')}"
                    ),
                    evidence_path=self.rel(annotation_json),
                    remediation="Fix annotation/completeness issues, regenerate the annotation report, and rerun the gate.",
                )
                for check in failing_checks
            ]
            status = PASS if result == "PASS" and not blockers else FAIL
            return self.make_result(
                status,
                f"Annotation report result is {result or 'UNKNOWN'}.",
                blockers=blockers,
                evidence=evidence,
                details={"summary": summary, "counts": counts, "failing_check_count": len(failing_checks)},
            )

        references = self._extract_references(schematic_files[0])
        duplicates = {ref: count for ref, count in references.items() if count > 1}
        unresolved = [ref for ref in references if "?" in ref or ref.startswith("*")]
        blockers = []
        for ref, count in duplicates.items():
            blockers.append(
                GateBlocker(
                    id="DUPLICATE_REFERENCE",
                    severity="CRITICAL",
                    message=f"Reference {ref} appears {count} times.",
                    evidence_path=self.rel(schematic_files[0]),
                    remediation="Annotate the schematic so each component has a unique reference.",
                )
            )
        for ref in unresolved:
            blockers.append(
                GateBlocker(
                    id="UNRESOLVED_REFERENCE",
                    severity="CRITICAL",
                    message=f"Reference {ref} is unresolved.",
                    evidence_path=self.rel(schematic_files[0]),
                    remediation="Replace placeholder reference designators before layout.",
                )
            )
        if blockers:
            status = FAIL
            summary = "Fallback schematic scan found unresolved or duplicate references."
        else:
            status = INCOMPLETE
            summary = "No annotation report exists; fallback scan found no obvious reference blockers."
            blockers.append(
                self.missing_evidence_blocker(
                    "reports/ANNOTATION_CHECK.json",
                    "reports/ANNOTATION_CHECK.json",
                )
            )
        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"fallback_reference_count": len(references)},
        )

    def _extract_references(self, schematic: Path) -> dict[str, int]:
        content = self.read_text(schematic)
        refs = re.findall(r'\(property\s+"Reference"\s+"([^"]+)"', content)
        counts: dict[str, int] = {}
        for ref in refs:
            counts[ref] = counts.get(ref, 0) + 1
        return counts
