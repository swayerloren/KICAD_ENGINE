"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function parseArgs(argv) {
  const args = {
    live: false,
    url: "",
    source: "UNKNOWN",
    out: "",
    downloadPdf: false,
    confirmRedistributionRisk: false,
    waitMs: 2500
  };
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--live") args.live = true;
    else if (arg === "--url") args.url = argv[++i] || "";
    else if (arg === "--source") args.source = argv[++i] || "UNKNOWN";
    else if (arg === "--out") args.out = argv[++i] || "";
    else if (arg === "--download-pdf") args.downloadPdf = true;
    else if (arg === "--confirm-redistribution-risk") args.confirmRedistributionRisk = true;
    else if (arg === "--wait-ms") args.waitMs = Number(argv[++i] || "2500");
  }
  return args;
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function blockedText(text) {
  return /(captcha|verify you are human|access denied|login required|sign in|create an account|blocked|too many requests)/i.test(text);
}

async function runLive(args, outDir) {
  if (!args.url.startsWith("https://")) {
    throw new Error("Live capture requires an explicit https:// public page URL.");
  }
  if (args.downloadPdf && !args.confirmRedistributionRisk) {
    throw new Error("--download-pdf requires --confirm-redistribution-risk. PDF download is still not implemented by this script.");
  }
  let chromium;
  try {
    chromium = require("playwright").chromium;
  } catch (error) {
    throw new Error("Playwright is not installed. Install it intentionally before using --live. Dry-run mode does not require it.");
  }

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ storageState: undefined });
  const page = await context.newPage();
  const result = {
    status: "LIVE_PUBLIC_PAGE",
    source: args.source,
    source_url: args.url,
    retrieved_at: new Date().toISOString(),
    live_web_used: true,
    pdfs_downloaded: false,
    verification_status: "UNVERIFIED",
    human_review_required: true,
    stopped_reason: ""
  };

  try {
    await page.goto(args.url, { waitUntil: "domcontentloaded", timeout: 30000 });
    await page.waitForTimeout(args.waitMs);
    const text = await page.locator("body").innerText({ timeout: 5000 }).catch(() => "");
    if (blockedText(text)) {
      result.status = "BLOCKED_OR_LOGIN_REQUIRED";
      result.stopped_reason = "Page text indicated CAPTCHA, login, access denial, or blocking.";
    }
    result.title = await page.title().catch(() => "");
    result.visible_text_excerpt = text.slice(0, 1000);
    const screenshotPath = path.join(outDir, "public_page_screenshot.png");
    await page.screenshot({ path: screenshotPath, fullPage: true });
    result.screenshot_path = path.relative(ROOT, screenshotPath);
  } finally {
    await browser.close();
  }
  return result;
}

async function main() {
  const args = parseArgs(process.argv);
  const outDir = args.out ? path.resolve(args.out) : path.join(ROOT, "evidence", timestamp());
  ensureDir(outDir);

  if (!args.live) {
    const dryRun = {
      status: "DRY_RUN_ONLY",
      source: args.source,
      planned_url: args.url || "UNSPECIFIED",
      generated_at: new Date().toISOString(),
      live_web_used: false,
      pdfs_downloaded: false,
      verification_status: "UNVERIFIED",
      human_review_required: true,
      notes: [
        "No browser was launched.",
        "Pass --live only for public pages and after source-profile review.",
        "Stop on CAPTCHA, login, blocking, or unclear terms."
      ]
    };
    const outPath = path.join(outDir, "public_page_capture_dry_run.json");
    fs.writeFileSync(outPath, JSON.stringify(dryRun, null, 2) + "\n");
    console.log(`DRY_RUN evidence plan written: ${outPath}`);
    return;
  }

  const result = await runLive(args, outDir);
  const outPath = path.join(outDir, "public_page_capture.json");
  fs.writeFileSync(outPath, JSON.stringify(result, null, 2) + "\n");
  console.log(`Evidence written: ${outPath}`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
