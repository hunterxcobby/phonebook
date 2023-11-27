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
    start_row = height // 2 + 4

    for idx, item in enumerate(menu, start=start_row):
        stdscr.addstr(idx, (width - len(item)) // 2, item)

    stdscr.refresh()

def print_mail_info(stdscr):
    mail_info = "Mail: solomonsefah13@gmail.com"

    height, width = stdscr.getmaxyx()
    mail_row = height - 1
    mail_col = 0

    stdscr.addstr(mail_row, mail_col, mail_info.encode('utf-8').decode('utf-8', 'half'))
    stdscr.refresh()


def version_model(stdscr):
    # Print contacts model information at the top right corner
    contacts_model = "cli phonebook v1.0"
    height, width = stdscr.getmaxyx()
    model_row = 0
    model_col = 0  # Adjust the '2' for spacing
    stdscr.addstr(model_row, model_col, contacts_model)
    stdscr.refresh()

