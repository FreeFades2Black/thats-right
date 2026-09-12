import os
import re
import pytest

def test_readme_exists():
    assert os.path.exists("README.md"), "README.md must exist"

def test_achievement_entries_structure():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    entries = re.findall(r"Pull Shark.*Milestone.*#(\d+)", content)
    assert len(entries) > 0, "Should have tracked milestones"
    # Ensure all extracted milestones are valid numeric IDs
    for entry in entries:
        assert int(entry) > 0

def test_milestone_files_integrity():
    for i in range(1, 87):
        filename = f"max_{i}.txt"
        assert os.path.exists(filename), f"{filename} must exist"
        with open(filename, "r", encoding="utf-8") as f:
            line = f.read().strip()
            assert f"maxing shark {i}" in line or "shark" in line.lower()
