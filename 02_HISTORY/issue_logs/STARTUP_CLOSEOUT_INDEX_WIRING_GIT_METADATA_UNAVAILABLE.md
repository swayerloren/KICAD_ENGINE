# Issue Log: Git Metadata Unavailable During Startup Wiring

Date: 2026-05-03
Status: OPEN
Severity: LOW
Scope: Repo tooling and release workflow readiness.

## Issue

`git status --short` failed with:

`fatal: not a git repository (or any of the parent directories): .git`

## Why It Matters

Startup and closeout can operate without Git metadata, but public release work, commits, diffs, tags, GitHub Actions release validation, and repository status reporting need a confirmed Git worktree.

## Current Mitigation

The new index builders use filesystem scanning and do not require `.git`.

## Required Resolution

Before release automation, confirm one of these is true:

- The workspace is the real Git checkout and `.git` exists.
- The task is intentionally running inside an installer payload/template where `.git` is absent.
- Release commands are run from the correct Git worktree.

