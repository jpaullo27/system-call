import os

def clear():
    os.system('clear')

def help():
    print("""Commands:
touch <file_name> - Create a new file
echo <file_name> <new_content> - Edit a file
mkdir <directory_name> - Create a new directory
ls - List files and directories
cat <file_name> - Display file content
rm <file_name> - Remove a file
exit - Exit the program
clear - Clear the screen""")

def remove_file(name_file):
    try:
        os.remove(name_file)
        print("File Removed Successfully!")
    except FileNotFoundError:
        print("\033[31mFile not found!\033[m")

def edit_file(name_file, new_content):
    try:
        with open(name_file, "w") as file:
            file.write(new_content)
        print("File Modified Successfully!")
    except FileNotFoundError:
        print("\033[31mFile not found!\033[m")

def make_dir(name_directory):
    try:
        os.mkdir(name_directory)
        print("Directory Created Successfully!")
    except OSError:
        print("\033[31mError creating directory!\033[m")

def create_file(name_file, content):
    try:
        with open(name_file, "w") as file:
            file.write(content)
        print("File Created Successfully!")
    except OSError:
        print("\033[31mError creating file!\033[m")

def list_files():
    try:  
        os.system('ls')
    except OSError:
        print("\033[31mError listing files!\033[m")

def cat_file(name_file):
    try:
        with open(name_file, "r") as file:
            content = file.read()
            print(content)
    except OSError:
        print("\033[31mError reading file!\033[m")

def execute_command(command_input):
    parts = command_input.split()
    command = parts[0]
    args = parts[1:]

    if command == 'touch':
        if len(args) != 1:
            print("\033[31mUsage: touch <file_name>\033[m")
            return
        name_file = args[0]
        create_file(name_file, "só alegria hahaha")
    elif command == 'echo':
        if len(args) < 2:
            print("\033[31mUsage: echo <file_name> <new_content>\033[m")
            return
        name_file = args[0]
        new_content = ' '.join(args[1:])
        edit_file(name_file, new_content)
    elif command == 'mkdir':
        if len(args) != 1:
            print("\033[31mUsage: mkdir <directory_name>\033[m")
            return
        name_directory = args[0]
        make_dir(name_directory)
    elif command == 'ls':
        list_files()
    elif command == 'exit':
        exit()
    elif command == 'clear':
        clear()
    elif command == 'cat':
        if len(args) != 1:
            print("\033[31mUsage: cat <file_name>\033[m")
            return
        name_file = args[0]
        cat_file(name_file)
    elif command == 'rm':
        if len(args) != 1:
            print("\033[31mUsage: rm <file_name>\033[m")
            return
        name_file = args[0]
        remove_file(name_file)
    elif command == 'help':
        help()

def main():
    try: 
        execute_command('help')
        while True:
            choice = input("> ")
            execute_command(choice)
    except KeyboardInterrupt:
        pass
    print("\n\033[33mprograma Encerrado!\033[m")

main()
