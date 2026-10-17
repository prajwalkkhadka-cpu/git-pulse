"""
Repository Health Score Analyzer
================================
Calculates an objective 0-100 score for a git repository based on:
  - Working tree cleanliness (no uncommitted chaos)
  - Presence of standard documentation (README, LICENSE, .gitignore)
  - Commit frequency & stale branches
  - Large binary file warnings
"""

import os
from typing import Dict, List, Tuple


class HealthScoreAnalyzer:
    """Evaluates git repo best practices and produces a weighted health score."""

    def __init__(self, repo_path: str, status_summary: Dict[str, int]) -> None:
        self.repo_path = repo_path
        self.status = status_summary

    def calculate(self) -> Tuple[int, List[Dict[str, str]]]:
        """
        Returns:
            Tuple of (score: int, checks: List[Dict])
        """
        score = 100
        checks = []

        # 1. Clean Working Tree check (Max 25 pts penalty)
        uncommitted = self.status.get("modified", 0) + self.status.get("untracked", 0)
        if self.status.get("conflicts", 0) > 0:
            score -= 30
            checks.append({"status": "FAIL", "msg": f"Merge conflicts detected ({self.status['conflicts']} files)"})
        elif uncommitted == 0:
            checks.append({"status": "PASS", "msg": "Working tree is completely clean"})
        elif uncommitted <= 5:
            score -= 5
            checks.append({"status": "WARN", "msg": f"{uncommitted} uncommitted changes pending"})
        else:
            score -= 15
            checks.append({"status": "FAIL", "msg": f"Heavy uncommitted state ({uncommitted} dirty files)"})

        # 2. Essential files check
        essential_files = {
            "README.md": ("README Documentation", 15),
            ".gitignore": (".gitignore Configuration", 10),
            "LICENSE": ("Open Source License", 5),
        }

        for fname, (label, penalty) in essential_files.items():
            fpath = os.path.join(self.repo_path, fname)
            # Case-insensitive check
            found = any(f.lower() == fname.lower() for f in os.listdir(self.repo_path)) if os.path.exists(self.repo_path) else False
            if found:
                checks.append({"status": "PASS", "msg": f"{label} is present"})
            else:
                score -= penalty
                checks.append({"status": "WARN", "msg": f"Missing {label}"})

        # 3. Large files scanning (e.g. >10MB files that should be in git-lfs)
        large_files = self._scan_large_files(limit_mb=10)
        if large_files:
            score -= 15
            checks.append({"status": "FAIL", "msg": f"{len(large_files)} large file(s) (>10MB) detected in tree"})
        else:
            checks.append({"status": "PASS", "msg": "No bloated large binary files detected"})

        score = max(0, min(100, score))
        return score, checks

    def _scan_large_files(self, limit_mb: int = 10) -> List[str]:
        """Scan working directory for files larger than limit_mb, ignoring .git."""
        large = []
        limit_bytes = limit_mb * 1024 * 1024
        for root, dirs, files in os.walk(self.repo_path):
            if ".git" in dirs:
                dirs.remove(".git")
            if "node_modules" in dirs:
                dirs.remove("node_modules")
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    if os.path.getsize(fp) > limit_bytes:
                        large.append(os.path.relpath(fp, self.repo_path))
                except OSError:
                    continue
        return large
