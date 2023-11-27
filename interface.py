#!/usr/bin/env python3

import curses
import subprocess
from menu import print_menu, print_author_info, version_model


def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()

    #Call the function with the animated start page
    print_menu(stdscr)

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Define the window size
    window = stdscr.subwin(height - 1, width - 1, 0, 0)

    # Enable keypad input
    stdscr.keypad(1)

    # Refresh the screen
    stdscr.refresh()

    # Print menu, author info, and contacts model
    print_menu(stdscr)
    print_author_info(stdscr)
    version_model(stdscr)

    while True:
        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == ord('s'):
            # Run a C program in a new tmux window
            run_c_program_in_tmux()
        elif key == ord('q'):
            # Quit the program
            break

    # Clean up
    curses.endwin()

def run_c_program_in_tmux():
    program_path = './phonebook'
    
    try:
        # Launch a new tmux window and run the C program
        subprocess.run([program_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error launching tmux for {program_path}")

if __name__ == "__main__":
    curses.wrapper(main)
