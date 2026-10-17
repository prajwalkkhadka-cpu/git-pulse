# ⚡ git-pulse

> **The Aesthetic Git Terminal Dashboard & Repository Health Analyzer**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Linux%20|%20Windows-brightgreen.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

`git-pulse` replaces raw, boring `git status` outputs with an **interactive, hyper-aesthetic terminal HUD** for developers. It audits your repository hygiene, tracks commit velocity, previews uncommitted changes, and scores your repository health in real-time.

---

## 📸 Terminal Preview

```text
   ____ _ _               ____        _             
  / ___(_) |_            |  _ \ _   _| |___  ___   
 | |  _| | __|   _____   | |_) | | | | / __|/ _ \  
 | |_| | | |_   |_____|  |  __/| |_| | \__ \  __/  
  \____|_|\__|           |_|    \__,_|_|___/\___|  
       ⚡ The Real-Time Developer Git Dashboard

  📂 Repository : /home/developer/workspace/git-pulse
  🌿 Active Branch: main  │  📦 Commits: 148
  ─────────────────────────────────────────────────────────────────

  📊 WORKING TREE STATUS
    • Staged Changes   :   3
    • Modified Unstaged:   2
    • Untracked Files  :   1
  ─────────────────────────────────────────────────────────────────

  🛡️  REPOSITORY HEALTH AUDIT
  Overall Score : [██████████████████████████░░] 95%

    [✔ PASS] README Documentation is present
    [✔ PASS] .gitignore Configuration is present
    [✔ PASS] Open Source License is present
    [✔ PASS] No bloated large binary files detected
    [▲ WARN] 5 uncommitted changes pending in staging
  ─────────────────────────────────────────────────────────────────

  🕒 RECENT COMMITS TIMELINE
    e83f2a1 │ prajwalkkhadka   │ feat: integrate health score telemetry  (12 mins ago)
    b2c9041 │ prajwalkkhadka   │ refactor: optimize subprocess stream     (2 hours ago)
    7a19ff2 │ sarah_dev        │ style: add TokyoNight terminal theme     (1 day ago)
  ─────────────────────────────────────────────────────────────────

  🔥 RECENT VELOCITY MATRIX (Past 14 Days)
    Mon  ░ ▒ ▓ █ ▓ ▒ █ ▓ █ ▒ ▓ █ ▓ █ 
    Wed  ▒ ▓ ░ ▓ █ █ ▒ ▓ ▓ █ ▒ ▓ █ ▓ 
    Fri  ▓ █ ▒ █ ▓ ▒ ▓ █ █ ▓ █ ▒ ▓ █ 
    Sun  ▒ ▓ █ ▒ ▓ █ ▓ ▒ ▓ █ ▓ █ ▒ ▓ 

    Less ░ ▒ ▓ █ More
```

---

## ✨ Features

- 🛡️ **Repo Health Auditor**: Instant 0–100 score evaluating unstaged debt, missing documentation (`README`, `LICENSE`), and git bloat.
- 📦 **Zero External Overhead**: Native subprocess wrapper without requiring heavy third-party git bindings.
- 🔥 **Commit Velocity Grid**: Terminal-rendered contribution heatmap showing author velocity over the last two weeks.
- 🌿 **Branch & Working Tree Telemetry**: Clean visualization of staged, unstaged, untracked, and conflicting files at a single glance.
- 🎨 **Synthwave / Nord ANSI Styling**: Works seamlessly on iTerm2, Alacritty, Kitty, Windows Terminal, and Linux Bash/Zsh.

---

## 🚀 Quickstart & Installation

### Option 1: Run Instantly (No Installation Needed)

```bash
# Clone and run immediate interactive demo
git clone https://github.com/prajwalkkhadka-cpu/git-pulse.git
cd git-pulse
python demo.py
```

### Option 2: Install via pip

```bash
git clone https://github.com/prajwalkkhadka-cpu/git-pulse.git
cd git-pulse
pip install -e .

# Run in any git repository on your machine!
git-pulse
```

---

## 🛠️ CLI Options

```bash
# Analyze current repository
git-pulse

# Analyze a specific project folder
git-pulse /path/to/another/repo

# Check version
git-pulse --version
```

---

## 🧪 Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/prajwalkkhadka-cpu/git-pulse/issues).

---

## 👤 Author

**Prajwal Khadka**
- GitHub: [@prajwalkkhadka-cpu](https://github.com/prajwalkkhadka-cpu)
- Email: [prajwalkhadkcr7@gmail.com](mailto:prajwalkhadkcr7@gmail.com)

---

## ⭐️ Show Your Support

Give a ⭐️ if this project helped you keep your git repos clean and beautiful!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
