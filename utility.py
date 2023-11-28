# utility.py

import curses
import time

def print_loading(stdscr):
    height, width = stdscr.getmaxyx()
    loading_row = height // 2
    loading_col = (width - len("Loading...")) // 2

    stdscr.addstr(loading_row, loading_col, "Loading...")
    stdscr.refresh()

def loading_animation(stdscr):
    height, width = stdscr.getmaxyx()
    loading_row, loading_col = height // 2, width // 2  # Unpack the tuple

    animation_frames = "|/-\\"

    # Display "Loading..." with animation for 3 seconds
    for _ in range(7):
        for frame in animation_frames:
            stdscr.clear()
            print_loading(stdscr)
            stdscr.addstr(loading_row + 1, loading_col, f"Please wait {frame}")
            stdscr.refresh()
            time.sleep(0.1)

    # Clear the screen
    stdscr.clear()
    stdscr.refresh()