import shutil

def print_dashes():
    dash = '-'

    try:
        column = shutil.get_terminal_size().columns

        print(dash * column)
    except OSError:
        print(dash * 97)

def print_equals():
    equal = '='

    try:
        column = shutil.get_terminal_size().columns

        print(equal * column)
    except OSError:
        print(equal * 97)

def main_menu():
    print('\033[1m' + 'Main Menu' + '\033[0m')
    print("1. Login")
    print("2. Create and Account")
    print("3. Forgot Password")
    print("4. About the Game")
    print("5. Exit Game")
    choice = int(input("Please enter the corresponding number to where you'd like to go: "))
    return choice




print('')
print('\033[1m' + 'HELLO WELCOME TO ZOMBIE OVERFLOW!' + '\033[0m')
print('')
choice = 0

while(choice != 5):
    choice = main_menu()
    
