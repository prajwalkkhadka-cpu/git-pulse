"""
Terminal Color Palette & UI Theme
=================================
Handcrafted ANSI styling without hard external dependencies.
"""

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

# Modern Synthwave/Nord Palette
CYAN = "\033[38;5;81m"
GREEN = "\033[38;5;120m"
YELLOW = "\033[38;5;221m"
RED = "\033[38;5;203m"
PURPLE = "\033[38;5;141m"
BLUE = "\033[38;5;75m"
GRAY = "\033[38;5;244m"
DARK_GRAY = "\033[38;5;238m"


def colorize(text: str, color_code: str, bold: bool = False) -> str:
    prefix = (BOLD if bold else "") + color_code
    return f"{prefix}{text}{RESET}"


def health_color(score: int) -> str:
    if score >= 85:
        return GREEN
    elif score >= 60:
        return YELLOW
    return RED
