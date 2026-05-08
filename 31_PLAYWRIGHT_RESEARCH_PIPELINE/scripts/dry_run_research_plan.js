"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function parseArgs(argv) {
  const args = { live: false, target: null, out: null };
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--live") args.live = true;
    else if (arg === "--target") args.target = argv[++i];
    else if (arg === "--out") args.out = argv[++i];
  }
  return args;
}

function parseCsvLine(line) {
  const cells = [];
  let current = "";
  let quoted = false;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (ch === '"' && line[i + 1] === '"') {
      current += '"';
      i += 1;
    } else if (ch === '"') {
      quoted = !quoted;
    } else if (ch === "," && !quoted) {
      cells.push(current);
      current = "";
    } else {
      current += ch;
    }
  }
  cells.push(current);
  return cells;
}

function readCsv(filePath) {
  const text = fs.readFileSync(filePath, "utf8").trim();
  if (!text) return [];
  const lines = text.split(/\r?\n/).filter(Boolean);
  const headers = parseCsvLine(lines.shift());
  return lines.map((line) => {
    const row = {};
    const cells = parseCsvLine(line);
    headers.forEach((header, index) => {
      row[header] = cells[index] || "";
    });
    return row;
  });
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function main() {
  const args = parseArgs(process.argv);
  if (args.live) {
    console.error("dry_run_research_plan.js never performs live web access. Remove --live.");
    process.exit(2);
  }

  const targetFiles = args.target
    ? [path.resolve(args.target)]
    : fs.readdirSync(path.join(ROOT, "research_targets"))
        .filter((name) => name.endsWith(".csv"))
        .map((name) => path.join(ROOT, "research_targets", name));

  const records = [];
  for (const filePath of targetFiles) {
    for (const row of readCsv(filePath)) {
      records.push({
        ...row,
        target_file: path.relative(ROOT, filePath),
        mode: "DRY_RUN",
        planned_outputs: (row.required_outputs || "").split(";").filter(Boolean),
        verification_status: "UNVERIFIED",
        human_review_required: true,
        notes: row.notes || ""
      });
    }
  }

  const stamp = timestamp();
  const outDir = args.out ? path.resolve(args.out) : path.join(ROOT, "output", stamp);
  ensureDir(outDir);
  ensureDir(path.join(ROOT, "reports"));

  const plan = {
    status: "DRY_RUN_ONLY",
    generated_at: new Date().toISOString(),
    target_count: records.length,
    live_web_used: false,
    pdfs_downloaded: false,
    records
  };

  const jsonPath = path.join(outDir, "research_plan.json");
  fs.writeFileSync(jsonPath, JSON.stringify(plan, null, 2) + "\n");

  const reportPath = path.join(ROOT, "reports", `DRY_RUN_RESEARCH_PLAN_${stamp}.md`);
  const lines = [
    "# Dry-Run Research Plan",
    "",
    `Generated: ${plan.generated_at}`,
    "Status: `DRY_RUN_ONLY`",
    "",
    `- Target count: ${records.length}`,
    "- Live web used: `false`",
    "- PDFs downloaded: `false`",
    "",
    "| Priority | Vendor | Part | Category | Preferred Sources | Outputs |",
    "| --- | --- | --- | --- | --- | --- |"
  ];
  for (const record of records) {
    lines.push(`| ${record.priority} | ${record.vendor} | ${record.part_number} | ${record.category} | ${record.preferred_sources} | ${record.required_outputs} |`);
  }
  fs.writeFileSync(reportPath, `${lines.join("\n")}\n`);
  console.log(`DRY_RUN plan written: ${jsonPath}`);
  console.log(`Report written: ${reportPath}`);
}

main();
