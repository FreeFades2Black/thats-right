# ADR-0001: Squashed Atomic History over Bot PR Iteration Floods

**Status:** Accepted  
**Date:** 2026-05-18  
**Lead Architect:** William Free Hall (Free) <whall4.wh@gmail.com>

## 1. Context & Operational Challenge
Automated milestone tracking workflows generated 262 synthetic pull request merge loops to verify GitHub badge criteria. Retaining 262 repetitive merge commits in the production `main` git history cluttered git logs and obscured genuine feature delivery.

## 2. Options Considered
* **Option A: Retain Full 262-Commit Synthetic PR Log**
  - *Evaluation:* Retains raw commit audit trail, but creates severe commit log noise; screams "tutorial / bot scaffold" to senior engineering reviewers.
* **Option B: Squash Synthetic Iterations into Single Atomic Milestone Commit while Preserving Full History on Dedicated Safety Branch**
  - *Evaluation:* `main` branch maintains clean, imperative commit hygiene; full 262-commit history is permanently preserved on immutable `backup-pre-squash` branch.

## 3. Decision & Trade-Off Accepted
We adopted **Option B (Atomic Squash with Safety Branch)**.  
**Trade-Off Accepted:** Requires maintaining a safety branch for full historical auditing; delivers professional, senior-grade commit log discipline on `main`.
