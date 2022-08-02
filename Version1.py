def get_name(): #gets user's name, calls printing function
    first_name = input("Please enter your first name: ").strip()
    last_name = input("please enter your last name: ").strip()
    concat_name(first_name, last_name)

def concat_name(first, last): # concatenates first and last names into a full name
    full_name = first.capitalize(), last.capitalize()
    print_name(full_name)

def print_name(name): # prints name stripped
    print(f'Hello and welcome {name} !')

get_name() # begins code


