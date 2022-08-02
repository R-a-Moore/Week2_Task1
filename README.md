# Version 1 & Version 2

In this task, the code gathers the user's name, by first assigning it, then reassigning it into a full name and printing it capitalized at the beginning of each word, removing all white spaces.

This part of the code gets the user's name (first & last), cutting off all white space. Then calls to the `concat_name()` function.
```commandline
def get_name(): #gets user's name, calls printing function
    first_name = input("Please enter your first name: ").strip()
    last_name = input("please enter your last name: ").strip()
    concat_name(first_name, last_name)
```

this function capitalizes the first letters of each name, before concatinating them togehter into 1 full name variable. Then calls to the `print_name()` function.
```commandline
def concat_name(first, last): # concatenates first and last names into a full name
    full_name = first.capitalize(), last.capitalize()
    print_name(full_name)
```

This function prints out the full name
```commandline
def print_name(name): # prints name stripped
    print(f'Hello and welcome {name} !')
```

this line begins the code from the `get_name()` function
```commandline
get_name() # begins code
```

## Acceptance Criteria (DOD)
- define variable name
- defines variablefull_name
- re assigns name & full_name
- capitalizes names