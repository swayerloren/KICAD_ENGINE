"""SCHEMATIC_VISUAL_GATE."""

from __future__ import annotations

from .base_gate import BLOCKED, INCOMPLETE, PASS, BaseGate, GateBlocker


class SchematicVisualGate(BaseGate):
    gate_id = "SCHEMATIC_VISUAL_GATE"
    gate_name = "Schematic Visual Gate"
    stage = 3

    def evaluate(self):
        report = self.first_existing("reports/CLOSE_UP_REVIEW.md")
        full_page_dir = self.project_file("_verification", "schematic_visual", "full_page")
        crops_dir = self.project_file("_verification", "schematic_visual", "crops")
        full_page_files = []
        if full_page_dir.exists():
            for pattern in ("*.svg", "*.png", "*.pdf"):
                full_page_files.extend(sorted(full_page_dir.glob(pattern)))
        crop_files = []
        if crops_dir.exists():
            for pattern in ("*.svg", "*.png"):
                crop_files.extend(sorted(crops_dir.glob(pattern)))

        evidence = [
            self.evidence_path("schematic_closeup_review", report),
            self.evidence_path("schematic_full_page_dir", full_page_dir, kind="directory"),
            self.evidence_path("schematic_crops_dir", crops_dir, kind="directory"),
        ]
        blockers = []
        if not report:
            blockers.append(self.missing_evidence_blocker("schematic close-up review", "reports/CLOSE_UP_REVIEW.md"))
        if not full_page_files:
            blockers.append(self.missing_evidence_blocker("schematic full-page visual export", "_verification/schematic_visual/full_page"))
        if not crop_files:
            blockers.append(self.missing_evidence_blocker("schematic close-up crops", "_verification/schematic_visual/crops"))
        if blockers:
            return self.make_result(
                INCOMPLETE,
                "Schematic visual evidence is incomplete.",
                blockers=blockers,
                evidence=evidence,
                details={"full_page_file_count": len(full_page_files), "crop_file_count": len(crop_files)},
            )

        text = self.read_text(report)
        human_not_reviewed = "Human visual result: `NOT_REVIEWED`" in text or "NEEDS_REVIEW" in text
        if human_not_reviewed:
            blockers.append(
                GateBlocker(
                    id="SCHEMATIC_VISUAL_HUMAN_REVIEW_REQUIRED",
                    severity="HIGH",
                    message="Schematic close-up crops exist, but at least one human visual result remains NOT_REVIEWED or NEEDS_REVIEW.",
                    evidence_path=self.rel(report),
                    remediation="Complete visual review sections and rerun the gate.",
                )
            )
            status = BLOCKED
            summary = "Schematic visual evidence exists but human review remains required."
        else:
            status = PASS
            summary = "Schematic full-page export and close-up review evidence exist."

        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"full_page_file_count": len(full_page_files), "crop_file_count": len(crop_files)},
        )
