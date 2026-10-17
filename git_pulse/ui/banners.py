"""
Banners and ASCII Art
"""

from git_pulse.ui.theme import CYAN, GREEN, PURPLE, RESET, BOLD

LOGO = f"""{CYAN}{BOLD}
   ____ _ _               ____        _             
  / ___(_) |_            |  _ \ _   _| |___  ___   
 | |  _| | __|   _____   | |_) | | | | / __|/ _ \  
 | |_| | | |_   |_____|  |  __/| |_| | \__ \  __/  
  \____|_|\__|           |_|    \__,_|_|___/\___|  
{RESET}{PURPLE}       ⚡ The Real-Time Developer Git Dashboard{RESET}
"""


def render_logo():
    print(LOGO)
