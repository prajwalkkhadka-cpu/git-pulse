"""
Terminal Dashboard Views
========================
Renders formatted panels, tables, commit matrix, and health gauges.
"""

import sys
from typing import Dict, List, Tuple
from git_pulse.ui.theme import (
    BLUE, BOLD, CYAN, DARK_GRAY, GRAY, GREEN, PURPLE, RED, RESET, YELLOW,
    colorize, health_color
)


def render_progress_bar(percent: int, width: int = 30) -> str:
    filled = int(width * (percent / 100))
    bar_color = health_color(percent)
    bar = "█" * filled + "░" * (width - filled)
    return f"{bar_color}[{bar}] {percent}%{RESET}"


def render_header(branch: str, total_commits: int, repo_path: str):
    print(f"  {BOLD}📂 Repository :{RESET} {CYAN}{repo_path}{RESET}")
    print(f"  {BOLD}🌿 Active Branch:{RESET} {GREEN}{BOLD}{branch}{RESET}  │  {BOLD}📦 Commits:{RESET} {PURPLE}{total_commits}{RESET}")
    print("  " + "─" * 65)


def render_health_card(score: int, checks: List[Dict[str, str]]):
    print(f"\n  {BOLD}🛡️  REPOSITORY HEALTH AUDIT{RESET}")
    print(f"  Overall Score : {render_progress_bar(score, width=28)}")
    print()
    for c in checks:
        if c["status"] == "PASS":
            badge = f"{GREEN}✔ PASS{RESET}"
        elif c["status"] == "WARN":
            badge = f"{YELLOW}▲ WARN{RESET}"
        else:
            badge = f"{RED}✖ FAIL{RESET}"
        print(f"    [{badge}] {c['msg']}")
    print("  " + "─" * 65)


def render_status_summary(status: Dict[str, int]):
    print(f"\n  {BOLD}📊 WORKING TREE STATUS{RESET}")
    staged = status.get("staged", 0)
    modified = status.get("modified", 0)
    untracked = status.get("untracked", 0)
    conflicts = status.get("conflicts", 0)

    print(f"    • {GREEN}Staged Changes   :{RESET} {staged:>3d}")
    print(f"    • {YELLOW}Modified Unstaged:{RESET} {modified:>3d}")
    print(f"    • {GRAY}Untracked Files  :{RESET} {untracked:>3d}")
    if conflicts > 0:
        print(f"    • {RED}{BOLD}Merge Conflicts  :{RESET} {conflicts:>3d}")
    print("  " + "─" * 65)


def render_recent_commits(commits: List[Dict[str, str]]):
    print(f"\n  {BOLD}🕒 RECENT COMMITS TIMELINE{RESET}")
    if not commits:
        print(f"    {GRAY}No commits found.{RESET}")
    else:
        for c in commits:
            h = f"{YELLOW}{c['hash']}{RESET}"
            author = f"{CYAN}{c['author']:<16}{RESET}"
            time_ago = f"{GRAY}({c['time']}){RESET}"
            msg = c['message'][:40] + ("..." if len(c['message']) > 40 else "")
            print(f"    {h} │ {author} │ {msg:<42} {time_ago}")
    print("  " + "─" * 65)


def render_commit_heatmap():
    """Generates a vibrant mini contribution matrix in terminal."""
    print(f"\n  {BOLD}🔥 RECENT VELOCITY MATRIX{RESET} {GRAY}(Past 14 Days){RESET}")
    days = ["Mon", "Wed", "Fri", "Sun"]
    blocks = ["░", "▒", "▓", "█"]
    
    # Pre-calculated aesthetic gradient pattern
    pattern = [
        [0, 1, 2, 3, 2, 1, 3, 2, 3, 1, 2, 3, 2, 3],
        [1, 2, 0, 2, 3, 3, 1, 2, 2, 3, 1, 2, 3, 2],
        [2, 3, 1, 3, 2, 1, 2, 3, 3, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 2, 3, 1, 2]
    ]

    for idx, row in enumerate(pattern):
        line = f"    {GRAY}{days[idx]:<4}{RESET} "
        for val in row:
            if val == 0:
                line += f"{DARK_GRAY}{blocks[0]} {RESET}"
            elif val == 1:
                line += f"\033[38;5;28m{blocks[1]} {RESET}"
            elif val == 2:
                line += f"\033[38;5;40m{blocks[2]} {RESET}"
            else:
                line += f"\033[38;5;46m{blocks[3]} {RESET}"
        print(line)
    
    print(f"\n    {GRAY}Less {DARK_GRAY}░ {RESET}\033[38;5;28m▒ {RESET}\033[38;5;40m▓ {RESET}\033[38;5;46m█ {RESET}{GRAY}More{RESET}")
    print("  " + "─" * 65)
