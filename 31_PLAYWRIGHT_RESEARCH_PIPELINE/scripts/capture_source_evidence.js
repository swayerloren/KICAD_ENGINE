"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function parseArgs(argv) {
  const args = { sourceUrl: "", sourceName: "UNKNOWN", partNumber: "UNKNOWN", out: "" };
  for (let i = 2; i < argv.length; i += 1) {
    if (argv[i] === "--source-url") args.sourceUrl = argv[++i] || "";
    else if (argv[i] === "--source-name") args.sourceName = argv[++i] || "UNKNOWN";
    else if (argv[i] === "--part-number") args.partNumber = argv[++i] || "UNKNOWN";
    else if (argv[i] === "--out") args.out = argv[++i] || "";
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  const outDir = args.out ? path.resolve(args.out) : path.join(ROOT, "evidence", timestamp());
  fs.mkdirSync(outDir, { recursive: true });
  const evidence = {
    status: "SOURCE_EVIDENCE_STUB",
    capture_mode: "DRY_RUN",
    part_number: args.partNumber,
    source_name: args.sourceName,
    source_url: args.sourceUrl || "UNKNOWN",
    retrieved_at: new Date().toISOString(),
    source_confidence: "UNKNOWN",
    verification_status: "UNVERIFIED",
    human_review_required: true,
    notes: "Created without live browsing. Fill after source-profile-compliant review."
  };
  const outPath = path.join(outDir, "source_evidence.json");
  fs.writeFileSync(outPath, JSON.stringify(evidence, null, 2) + "\n");
  console.log(`Source evidence stub written: ${outPath}`);
}

main();
