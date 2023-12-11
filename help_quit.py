#!/usr/bin/python3

import curses

menu = [
    "Add Contact",
    "Save Contacts",
    "Edit Contact",
    "Delete Contact",
    "Press q to Quit",
    "Press h for Help"
]

def print_phonebook_menu(stdscr, selected_option):
    # Print the phone book menu with the selected option highlighted

    # Calculate the starting row to center the menu
    height, width = stdscr.getmaxyx()
    start_row = max(0, (height - len(menu)) // 2)

    for idx, item in enumerate(menu, start=start_row + 1):
        if idx == selected_option:
            stdscr.addstr(idx, 2, item, curses.A_STANDOUT)
        else:
            stdscr.addstr(idx, 2, item)

    # Add "Quit" at the left bottom
    quit_text = "Quit"
    stdscr.addstr(height - 2, 2, quit_text, curses.A_STANDOUT if selected_option == len(menu) - 1 else curses.A_NORMAL)

    # Add "Help" at the right bottom
    help_text = "Help"
    stdscr.addstr(height - 2, width - len(help_text) - 2, help_text, curses.A_STANDOUT if selected_option == len(menu) else curses.A_NORMAL)

    stdscr.refresh()
