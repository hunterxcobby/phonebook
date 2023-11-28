# utility.py

import time

def print_loading(stdscr):
    height, width = stdscr.getmaxyx()
    loading_row = height // 2
    loading_col = (width - len(" ░L░O░A░D░I░N░G░")) // 2

    stdscr.addstr(loading_row, loading_col, " ░L░O░A░D░I░N░G░")
    stdscr.refresh()

def loading_animation(stdscr):
    height, width = stdscr.getmaxyx()
    loading_row, loading_col = height // 2, width // 2  # Unpack the tuple

    # Display "Loading..." with an interactive frame animation for 3 seconds
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]  # Use Unicode characters for a dynamic effect

    for _ in range(3):
        for frame in frames:
            stdscr.clear()
            print_loading(stdscr)
            stdscr.addstr(loading_row + 1, loading_col, f"{frame}")
            stdscr.refresh()
            time.sleep(0.15)

    # Clear the screen
    stdscr.clear()
    stdscr.refresh()

def print_quiting(stdscr):
    height, width = stdscr.getmaxyx()
    quiting_row = height // 2
    quiting_col = (width - len(" ░Q░U░I░T░T░I░N░G░")) // 2

    stdscr.addstr(quiting_row, quiting_col, " ░Q░U░I░T░T░I░N░G░")
    stdscr.refresh()

def quit_loading(stdscr):
    height, width = stdscr.getmaxyx()
    quiting_row, quiting_col = height // 2, width // 2  # Unpack the tuple

    # Display "Loading..." with an interactive frame animation for 3 seconds
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]  # Use Unicode characters for a dynamic effect

    for _ in range(3):
        for frame in frames:
            stdscr.clear()
            print_quiting(stdscr)
            stdscr.addstr(quiting_row + 1, quiting_col, f"{frame}")
            stdscr.refresh()
            time.sleep(0.15)

    # Clear the screen
    stdscr.clear()
    stdscr.refresh()