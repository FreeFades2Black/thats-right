# Operational Runbook: GitHub Achievement Criteria Verification Triage

**Severity:** P3 / Verification Check  
**Target Systems:** GitHub API, Achievement Test Harness

## Diagnostic Workflow
1. Run automated achievement test suite:
   ```bash
   python -m pytest tests/test_achievements.py -v
   ```
2. Verify milestone metadata tags:
   ```bash
   git tag -l -n
   ```
