import utils
import sys

def abuse(): # dry code is good code
    print("When running this command, please enter 'build' or 'new' as an argument (An argument?... but I came here for abuse!)")

print("This is argv:", sys.argv[0])

if len(sys.argv) < 2: # making it so if the user doesn't enter any arguments on the command line they get instructions
    abuse()
else:
    command = sys.argv[1]
    if command == "build": # creates pages when user uses build argument
        utils.create_pages()
        print('Pages created')
    elif command == "new": # allows user to create new page for site
        utils.new_page()
    else:
        abuse() # instructional message if invalid argument is given
