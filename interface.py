#!/usr/bin/env python3

import curses
import subprocess
import time
from menu import print_menu, print_mail_info, version_model
from utility import print_loading, loading_animation

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()    

    # Set the background color to cyan
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    stdscr.bkgd(curses.color_pair(1))

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
    print_mail_info(stdscr)

    version_model(stdscr)

    while True:
        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == curses.KEY_ENTER or key == 10:
            time.sleep(0.5)
            print_loading(stdscr)

            loading_animation(stdscr)
            time.sleep(1)
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
        print(f"Error starting program {program_path}")
        print("Please restart...")

if __name__ == "__main__":
    curses.wrapper(main)
