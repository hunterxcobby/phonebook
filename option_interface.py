# phonebook_interface.py

import curses

def print_phonebook_menu(stdscr):
    # Print the phone book menu
    menu = [
        "Phonebook Options",
        "1. Add Contact",
        "2. Save Contacts",
        "3. Edit Contact",
        "4. Delete Contact",
        "Press q to go back"
    ]

    for idx, item in enumerate(menu, start=1):
        stdscr.addstr(idx, 2, item)

    stdscr.refresh()

def phonebook_interface(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Define the window size
    window = stdscr.subwin(height - 1, width - 1, 0, 0)

    # Enable keypad input
    stdscr.keypad(1)

    # Refresh the screen
    stdscr.refresh()

    while True:
        # Display phone book menu
        print_phonebook_menu(stdscr)

        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == ord('1'):
            # Add contact logic (you can implement this)
            pass
        elif key == ord('2'):
            # Save contacts logic (you can implement this)
            pass
        elif key == ord('3'):
            # Edit contact logic (you can implement this)
            pass
        elif key == ord('4'):
            # Delete contact logic (you can implement this)
            pass
        elif key == ord('q'):
            # Go back
            break

    # Clean up
    curses.endwin()

# You can add more functions for each specific action (add, save, edit, delete) in this module
