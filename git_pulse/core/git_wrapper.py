"""
Git Wrapper Module
==================
Executes native git commands safely using standard library subprocess.
Provides structured data parsing without third-party heavy dependencies.
"""

import os
import subprocess
from typing import Dict, List, Optional, Tuple


class GitCommandError(Exception):
    """Raised when a git command exits with non-zero status."""
    pass


class GitWrapper:
    """Safe abstraction over system git CLI."""

    def __init__(self, repo_path: str = ".") -> None:
        self.repo_path = os.path.abspath(repo_path)

    def run(self, *args: str) -> str:
        """Run a git command and return stripped stdout."""
        cmd = ["git"] + list(args)
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
                encoding="utf-8",
                errors="replace",
            )
            if result.returncode != 0:
                raise GitCommandError(result.stderr.strip() or f"Git command failed: {' '.join(cmd)}")
            return result.stdout.strip()
        except FileNotFoundError:
            raise GitCommandError("git executable not found on system PATH.")

    def is_git_repository(self) -> bool:
        """Checks if target directory is inside a git work tree."""
        try:
            out = self.run("rev-parse", "--is-inside-work-tree")
            return out.strip().lower() == "true"
        except GitCommandError:
            return False

    def get_current_branch(self) -> str:
        """Returns the currently checked out branch name or commit hash (if detached)."""
        try:
            return self.run("rev-parse", "--abbrev-ref", "HEAD")
        except GitCommandError:
            return "unknown"

    def get_commit_count(self) -> int:
        """Returns total number of commits on current HEAD."""
        try:
            out = self.run("rev-list", "--count", "HEAD")
            return int(out)
        except (GitCommandError, ValueError):
            return 0

    def get_branches(self) -> List[Dict[str, str]]:
        """Returns list of local branches with their last commit date and upstream status."""
        try:
            format_str = "%(refname:short)|%(authordate:relative)|%(upstream:track)"
            raw = self.run("for-each-ref", "--sort=-committerdate", f"--format={format_str}", "refs/heads/")
            branches = []
            for line in raw.splitlines():
                if not line.strip():
                    continue
                parts = line.split("|")
                branches.append({
                    "name": parts[0],
                    "last_commit": parts[1] if len(parts) > 1 else "unknown",
                    "status": parts[2] if len(parts) > 2 and parts[2] else "up to date",
                })
            return branches
        except GitCommandError:
            return []

    def get_status_summary(self) -> Dict[str, int]:
        """Parses git status --porcelain to get counts of modified, staged, untracked files."""
        summary = {"staged": 0, "modified": 0, "untracked": 0, "conflicts": 0}
        try:
            raw = self.run("status", "--porcelain")
            for line in raw.splitlines():
                if len(line) < 2:
                    continue
                x, y = line[0], line[1]
                if x in ["M", "A", "D", "R"]:
                    summary["staged"] += 1
                if y == "M":
                    summary["modified"] += 1
                elif x == "?" and y == "?":
                    summary["untracked"] += 1
                elif x == "U" or y == "U":
                    summary["conflicts"] += 1
            return summary
        except GitCommandError:
            return summary

    def get_recent_commits(self, limit: int = 5) -> List[Dict[str, str]]:
        """Fetches recent commits with hash, author, relative time, and message."""
        try:
            raw = self.run("log", f"-n{limit}", "--pretty=format:%h|%an|%cr|%s")
            commits = []
            for line in raw.splitlines():
                if not line.strip():
                    continue
                parts = line.split("|", 3)
                if len(parts) == 4:
                    commits.append({
                        "hash": parts[0],
                        "author": parts[1],
                        "time": parts[2],
                        "message": parts[3],
                    })
            return commits
        except GitCommandError:
            return []

    def get_author_contributions(self, limit: int = 5) -> List[Tuple[str, int]]:
        """Returns top contributors sorted by number of commits."""
        try:
            raw = self.run("shortlog", "-sn", "--no-merges", "HEAD")
            authors = []
            for line in raw.splitlines()[:limit]:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    authors.append((parts[1], int(parts[0])))
            return authors
        except GitCommandError:
            return []
