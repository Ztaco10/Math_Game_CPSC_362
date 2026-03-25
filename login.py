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
    print('\033[1m' + "Main Menu" + '\033[0m')
    print("1. Login")
    print("2. Create and Account")
    print("3. Forgot Password")
    print("4. About the Game")
    print("5. Exit Game")
    choice = int(input("Please enter the corresponding number to where you'd like to go: "))
    return choice

def login():
    print('')
    print('\033[1m' + "Login Page" + '\033[0m')
    username = input("Enter username: ")
    password = input("Enter password: ")

def
    



print('')
print('\033[1m' + "HELLO WELCOME TO ZOMBIE OVERFLOW!" + '\033[0m')
print('')
choice = 0

while(True):
    choice = main_menu()

    if(choice == 1):
        login()
    elif(choice == 2):
        account_create()
    elif(choice == 3):
        password_change()
    elif(choice == 4):
        game_summary()
    elif(choice == 5):
        break
    else:
        print("PlThe choices are from numbers 1-5: ")

    
