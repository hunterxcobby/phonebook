# utility.py

def display_help(stdscr):
    # Function to display help information
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Print help content
    help_content = [
        "Phonebook Application Help",
        "---------------------------",
        "1. Add Contact: Allows you to add a new contact to the phonebook.\n",
        "2. Display Contact: Shows the list of all contacts in the phonebook.\n",
        "3. Search Contact: Search for a contact based on name or other criteria.\n",
        "4. Edit Contact: Modify existing contact information.\n",
        "5. Delete Contact: Remove a contact from the phonebook.",
        "6. Help: Display this help information.",
        "7. Exit: Quit the phonebook application.(Click twice if once does not work.\n)",
        "",
        "Use the arrow keys to navigate and press Enter to select an option.\n",
        "Press (q) to quit at any time.\n",
        "Press (h) to view this help information.\n",
        "---------------------------",
        "Press any key to return to the main menu...\n"
    ]

    for idx, line in enumerate(help_content, start=1):
        stdscr.addstr(idx, 2, line)

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before returning to the main menu
    stdscr.clear()
    stdscr.refresh()
