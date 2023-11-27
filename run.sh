#!/usr/bin/env bash

run_interface() 
{
    # Executes the python3 interface
    chmod +x "interface.py"
    python3 "interface.py"
}

compile_c()
{
    #compile the c program
    gcc *.c -o phonebook
}

# Call the function
run_interface
compile_c