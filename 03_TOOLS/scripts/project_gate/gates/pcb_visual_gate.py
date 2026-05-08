"""PCB_VISUAL_GATE."""

from __future__ import annotations

from .base_gate import BLOCKED, INCOMPLETE, PASS, BaseGate, GateBlocker


class PCBVisualGate(BaseGate):
    gate_id = "PCB_VISUAL_GATE"
    gate_name = "PCB Visual Gate"
    stage = 7

    def evaluate(self):
        report = self.first_existing("reports/PCB_CLOSE_UP_REVIEW.md")
        visual_dir = self.project_file("_verification", "pcb_visual")
        crops_dir = visual_dir / "crops"
        top_exports = []
        bottom_exports = []
        if visual_dir.exists():
            for pattern in ("*top*.svg", "*top*.png", "*F_Cu*.svg", "*F_Cu*.png"):
                top_exports.extend(sorted(visual_dir.glob(pattern)))
            for pattern in ("*bottom*.svg", "*bottom*.png", "*B_Cu*.svg", "*B_Cu*.png"):
                bottom_exports.extend(sorted(visual_dir.glob(pattern)))
        crop_files = []
        if crops_dir.exists():
            for pattern in ("*.svg", "*.png"):
                crop_files.extend(sorted(crops_dir.glob(pattern)))

        evidence = [
            self.evidence_path("pcb_closeup_review", report),
            self.evidence_path("pcb_visual_dir", visual_dir, kind="directory"),
            self.evidence_path("pcb_crops_dir", crops_dir, kind="directory"),
        ]
        blockers = []
        if not report:
            blockers.append(self.missing_evidence_blocker("PCB close-up review", "reports/PCB_CLOSE_UP_REVIEW.md"))
        if not top_exports:
            blockers.append(self.missing_evidence_blocker("PCB top visual export", "_verification/pcb_visual/*top*"))
        if not bottom_exports:
            blockers.append(self.missing_evidence_blocker("PCB bottom visual export", "_verification/pcb_visual/*bottom*"))
        if not crop_files:
            blockers.append(self.missing_evidence_blocker("PCB close-up crops", "_verification/pcb_visual/crops"))
        if blockers:
            return self.make_result(
                INCOMPLETE,
                "PCB visual evidence is incomplete.",
                blockers=blockers,
                evidence=evidence,
                details={"top_exports": len(top_exports), "bottom_exports": len(bottom_exports), "crop_files": len(crop_files)},
            )

        text = self.read_text(report)
        human_not_reviewed = "Human visual result: `NOT_REVIEWED`" in text or "NEEDS_REVIEW" in text
        if human_not_reviewed:
            blockers.append(
                GateBlocker(
                    id="PCB_VISUAL_HUMAN_REVIEW_REQUIRED",
                    severity="HIGH",
                    message="PCB close-up crops exist, but at least one human visual result remains NOT_REVIEWED or NEEDS_REVIEW.",
                    evidence_path=self.rel(report),
                    remediation="Complete PCB visual review sections and rerun the gate.",
                )
            )
            status = BLOCKED
            summary = "PCB visual evidence exists but human visual review remains required."
        else:
            status = PASS
            summary = "PCB top/bottom exports and close-up review evidence exist."

        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"top_exports": len(top_exports), "bottom_exports": len(bottom_exports), "crop_files": len(crop_files)},
        )
