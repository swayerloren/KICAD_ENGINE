"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function parseArgs(argv) {
  const args = { input: path.join(ROOT, "output"), out: "" };
  for (let i = 2; i < argv.length; i += 1) {
    if (argv[i] === "--input") args.input = argv[++i] || args.input;
    else if (argv[i] === "--out") args.out = argv[++i] || "";
  }
  return args;
}

function collectJsonFiles(target) {
  if (!fs.existsSync(target)) return [];
  const stat = fs.statSync(target);
  if (stat.isFile() && target.endsWith(".json")) return [target];
  if (!stat.isDirectory()) return [];
  return fs.readdirSync(target, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(target, entry.name);
    if (entry.isDirectory()) return collectJsonFiles(full);
    return entry.isFile() && entry.name.endsWith(".json") ? [full] : [];
  });
}

function main() {
  const args = parseArgs(process.argv);
  const input = path.resolve(args.input);
  const files = collectJsonFiles(input);
  fs.mkdirSync(path.join(ROOT, "reports"), { recursive: true });
  const outPath = args.out ? path.resolve(args.out) : path.join(ROOT, "reports", "RESEARCH_REPORT.md");
  const lines = [
    "# Research Report",
    "",
    `Generated: ${new Date().toISOString()}`,
    "Status: `DRY_RUN_OR_LOCAL_OUTPUT_SUMMARY`",
    "",
    `- Input: \`${input}\``,
    `- JSON files found: ${files.length}`,
    "",
    "| File | Status | Target Count | Notes |",
    "| --- | --- | ---: | --- |"
  ];
  for (const file of files) {
    let status = "UNKNOWN";
    let count = 1;
    let notes = "";
    try {
      const data = JSON.parse(fs.readFileSync(file, "utf8"));
      status = data.status || "JSON";
      count = Array.isArray(data.records) ? data.records.length : (Array.isArray(data) ? data.length : 1);
      notes = data.notes ? String(data.notes).slice(0, 100) : "";
    } catch (error) {
      status = "PARSE_ERROR";
      notes = error.message;
    }
    lines.push(`| \`${path.relative(ROOT, file)}\` | \`${status}\` | ${count} | ${notes} |`);
  }
  fs.writeFileSync(outPath, `${lines.join("\n")}\n`);
  console.log(`Research report written: ${outPath}`);
}

main();
