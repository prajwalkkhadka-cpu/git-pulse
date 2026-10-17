"""
Unit Tests for git-pulse
========================
"""

import pytest
from git_pulse.analyzers.health_score import HealthScoreAnalyzer
from git_pulse.ui.views import render_progress_bar


def test_progress_bar_bounds():
    bar_full = render_progress_bar(100, width=10)
    assert "100%" in bar_full

    bar_empty = render_progress_bar(0, width=10)
    assert "0%" in bar_empty


def test_health_analyzer_scoring():
    # Clean repo with no modifications
    status = {"modified": 0, "staged": 0, "untracked": 0, "conflicts": 0}
    analyzer = HealthScoreAnalyzer(".", status)
    score, checks = analyzer.calculate()

    assert score >= 0
    assert score <= 100
    assert len(checks) > 0


def test_conflict_penalty():
    status = {"modified": 2, "staged": 1, "untracked": 0, "conflicts": 2}
    analyzer = HealthScoreAnalyzer(".", status)
    score, checks = analyzer.calculate()

    # Conflicted repos should take severe penalty
    assert score <= 70
    fail_checks = [c for c in checks if c["status"] == "FAIL"]
    assert len(fail_checks) > 0
