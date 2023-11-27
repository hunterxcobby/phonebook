# this is for the menu of the phonebook
# Import necessary modules
import curses


def print_menu(stdscr):

    height, width = stdscr.getmaxyx()
    # Print a simple menu
    menu = [
        "Phonebook Interface",

        "Press s to start ",
        "Press q to quit",
    ]
    

    # Calculate the starting row for the menu to center it vertically
    start_row = height // 2 + 2

    for idx, item in enumerate(menu, start=start_row):
        stdscr.addstr(idx, (width - len(item)) // 2, item)

    stdscr.refresh()

def print_author_info(stdscr):
    # Print author information
    author_info = "Author: Your Name"
    stdscr.addstr(10, 2, author_info)
    stdscr.refresh()

def print_contacts_model(stdscr):
    # Print contacts model information
    contacts_model = "Contacts Model: Your Model"
    stdscr.addstr(11, 2, contacts_model)
    stdscr.refresh()