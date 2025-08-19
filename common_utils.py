import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def boolean_to_emooji(bool_val, primary_emooji: bool):
    if primary_emooji:
        return "✅" if bool_val else "❌"
    return "☑️" if bool_val else "✖️"


def confirm_exit_terminal():
    user_input = input('\n\nType "q" to exit.\n')
    if user_input != "q":
        return confirm_exit_terminal()
    else:
        sys.exit()
