import sys


def confirm_exit_terminal():
    user_input = input('\n\nType "q" to exit.\n')
    if user_input != "q":
        return confirm_exit_terminal()
    else:
        sys.exit()
