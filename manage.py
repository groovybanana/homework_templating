import utils
import sys

def abuse():
    print("When running this command, please enter 'build' or 'new' as an argument (An argument?... but I came here for abuse!)")

print("This is argv:", sys.argv[0])

if len(sys.argv) < 2:
    abuse()
else:
    command = sys.argv[1]
    if command == "build":
        utils.create_pages()
        print('Pages created')
    elif command == "new":
        utils.new_page()
    else:
        abuse()
