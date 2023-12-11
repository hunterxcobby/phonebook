# phonebook_interface.py

import curses
from utility import quit_loading

def print_phonebook_menu(stdscr, selected_option):
    # Print the phone book menu with the selected option highlighted
    menu = [
        "Add Contact",
        "Display Contact",
        "Search Contact",
        "Edit Contact",
        "Delete Contact",
    ]

    for idx, item in enumerate(menu, start=1):
        if idx == selected_option:
            stdscr.addstr(idx, 2, item, curses.A_STANDOUT)
        else:
            stdscr.addstr(idx, 2, item)

    # Print "Help" at the left bottom
    stdscr.addstr(curses.LINES - 1, 2, "HELP", curses.A_BOLD)

    # Print "Exit" at the right bottom
    stdscr.addstr(curses.LINES - 1, curses.COLS - 10, "EXIT", curses.A_BOLD)

    stdscr.refresh()

def phonebook_interface(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()

    # Enable keypad input
    stdscr.keypad(1)

    # Initialize selected option
    selected_option = 1

    while True:
        # Display phone book menu with the selected option highlighted
        print_phonebook_menu(stdscr, selected_option)

        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == curses.KEY_DOWN and selected_option < 5:
            selected_option += 1
        elif key == curses.KEY_UP and selected_option > 1:
            selected_option -= 1
        elif key == curses.KEY_ENTER or key == 10:
            # Perform action based on the selected option
            if selected_option == 1:
                # Add contact logic 
                pass
            elif selected_option == 2:
                # Display contacts logic
                pass
            elif selected_option == 3:
                # Search contact logic will be placed here 
                pass
            elif selected_option == 4:
                # Edit contact
                pass
            elif selected_option == 5:
                # Delete contact logic will go here 
                pass
            elif key == ord('h'):
                # Help logic will go here (triggered by pressing 'h')
                pass
            elif key == ord('q'):
                # Quit logic will go here (triggered by pressing 'q')
                quit_loading(stdscr)
                break

    # Clean up
    curses.endwin()
