# GitHub Actions Plan

Status: `PLANNED`

## Purpose

Define CI workflows for health checks, payload builds, installer builds, secret scans, checksums, and draft releases.

## Workflow Goals

- Build payload first.
- Run health checks.
- Run secret scan if available.
- Build platform installers on native runners.
- Upload artifacts.
- Generate SHA256 checksums.
- Draft releases only.

## Runners

- Windows: `windows-latest`
- macOS: `macos-latest`
- Linux: `ubuntu-latest`

## Safety

- Do not add secrets.
- Do not auto-publish releases.
- Do not require paid services.
- Do not store signing keys in the repo.

