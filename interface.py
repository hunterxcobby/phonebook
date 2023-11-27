#!/usr/bin/env python3

import curses
import subprocess

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Define the window size
    window = stdscr.subwin(height - 1, width - 1, 0, 0)

    # Enable keypad input
    stdscr.keypad(1)

    # Print a simple menu
    menu = ["Press s to start the phonebook", "Press q to quit"]
    for idx, item in enumerate(menu, start=1):
        stdscr.addstr(idx, 2, item)

    # Refresh the screen
    stdscr.refresh()

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
    # Replace 'your_program' with the actual name of your compiled C program
    program_path = './phonebook'
    
    try:
        # Launch a new tmux window and run the C program
        subprocess.run([program_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error launching tmux for {program_path}")

if __name__ == "__main__":
    curses.wrapper(main)
