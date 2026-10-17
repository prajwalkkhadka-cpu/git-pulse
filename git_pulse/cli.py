"""
Command Line Interface Entry Point
==================================
Routes subcommands, options, and handles interactive terminal flags.
"""

import argparse
import os
import sys

from git_pulse.core.git_wrapper import GitWrapper, GitCommandError
from git_pulse.analyzers.health_score import HealthScoreAnalyzer
from git_pulse.ui.banners import render_logo
from git_pulse.ui.theme import RED, YELLOW, RESET, BOLD
from git_pulse.ui.views import (
    render_header,
    render_health_card,
    render_status_summary,
    render_recent_commits,
    render_commit_heatmap,
)


def run_dashboard(path: str = "."):
    wrapper = GitWrapper(path)
    if not wrapper.is_git_repository():
        print(f"\n{RED}{BOLD}✖ Error:{RESET} '{os.path.abspath(path)}' is not a git repository.")
        print(f"Run {YELLOW}git-pulse --help{RESET} or initialize a repo using {YELLOW}git init{RESET}.\n")
        sys.exit(1)

    render_logo()

    branch = wrapper.get_current_branch()
    commit_count = wrapper.get_commit_count()
    render_header(branch, commit_count, os.path.abspath(path))

    # Working tree status
    status = wrapper.get_status_summary()
    render_status_summary(status)

    # Health evaluation
    analyzer = HealthScoreAnalyzer(path, status)
    score, checks = analyzer.calculate()
    render_health_card(score, checks)

    # Recent activity & velocity
    recent = wrapper.get_recent_commits(limit=5)
    render_recent_commits(recent)
    render_commit_heatmap()
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="git-pulse",
        description="⚡ git-pulse: Aesthetic Git Terminal Dashboard & Repository Health Analyzer",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to git repository (default: current directory)",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="git-pulse 1.0.0 by Prajwal Khadka (@prajwalkkhadka-cpu)",
    )

    args = parser.parse_args()
    run_dashboard(args.path)


if __name__ == "__main__":
    main()
