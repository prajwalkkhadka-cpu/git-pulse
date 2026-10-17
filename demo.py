"""
git-pulse Standalone Live Interactive Demo
==========================================
Zero dependencies required (Pure standard library).
Run instantly:
    python demo.py
"""

import time
import sys

from git_pulse.ui.banners import render_logo
from git_pulse.ui.theme import BOLD, CYAN, GREEN, PURPLE, RESET, YELLOW
from git_pulse.ui.views import (
    render_commit_heatmap,
    render_header,
    render_health_card,
    render_recent_commits,
    render_status_summary,
)


def run_demo():
    render_logo()
    print(f"  {YELLOW}⚡ Initializing repository telemetry & telemetry sensors...{RESET}", end="", flush=True)
    time.sleep(0.3)
    print(f" {GREEN}[OK]{RESET}\n")

    # Sample active repo state
    render_header("main", 148, "/home/developer/workspace/hyper-project")

    # Live status
    status = {"staged": 3, "modified": 2, "untracked": 1, "conflicts": 0}
    render_status_summary(status)

    # Health evaluation check
    checks = [
        {"status": "PASS", "msg": "README Documentation is present"},
        {"status": "PASS", "msg": ".gitignore Configuration is present"},
        {"status": "PASS", "msg": "Open Source License is present"},
        {"status": "PASS", "msg": "No bloated large binary files detected"},
        {"status": "WARN", "msg": "5 uncommitted changes pending in staging"},
    ]
    render_health_card(95, checks)

    # Commits timeline
    commits = [
        {"hash": "e83f2a1", "author": "prajwalkkhadka", "time": "12 minutes ago", "message": "feat: integrate real-time health score telemetry"},
        {"hash": "b2c9041", "author": "prajwalkkhadka", "time": "2 hours ago", "message": "refactor: optimize subprocess stream parsing"},
        {"hash": "7a19ff2", "author": "sarah_dev", "time": "1 day ago", "message": "style: add TokyoNight terminal color theme"},
        {"hash": "4d91e30", "author": "prajwalkkhadka", "time": "2 days ago", "message": "fix: avoid ANSI escape trailing artifact in Windows PS"},
        {"hash": "11ab9c8", "author": "alex_core", "time": "3 days ago", "message": "chore: initial commit and core wrapper logic"},
    ]
    render_recent_commits(commits)

    # Contribution matrix
    render_commit_heatmap()

    print(f"\n  {GREEN}{BOLD}🎉 Demo finished!{RESET} To analyze your current git repo, run: {CYAN}python -m git_pulse.cli .{RESET}\n")


if __name__ == "__main__":
    run_demo()
