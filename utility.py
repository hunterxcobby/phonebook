# utility.py

import curses
import time

def print_loading(stdscr):
    height, width = stdscr.getmaxyx()
    loading_row = height // 2
    loading_col = (width - len(" LOADING")) // 2

    stdscr.addstr(loading_row, loading_col, " LOADING")
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