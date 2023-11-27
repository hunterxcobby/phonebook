#!/usr/bin/env bash

run_interface() 
{
    # Executes the python3 interface
    chmod +x "interface.py"
    python3 "interface.py"
}

#!/usr/bin/env bash

compile_c() 
{
    # Compile the C program
    if gcc *.c -o phonebook; then
        echo "Compilation successful"
    else
        echo "Compilation failed"
        exit 1
    fi
}

# Call the function
run_interface
compile_c