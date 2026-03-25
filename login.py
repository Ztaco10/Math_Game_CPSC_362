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
    #check if the username exists

    password = input("Enter password: ")
    #check if the password matches the account



def account_create():
    print('')
    print('\033[1m' + "Account Creation Page" + '\033[0m')
    print("If you'd like to exit then please type '1' as username")
    
    username = input("Please enter a valid username: ")
    #check if the username already exists
    if(username == "1"):
        print("Exiting account creation menu")
        return



    password = input("Enter password: ")
    while(True):
        email_or_phone = input("Would you like to create your account with email or phone number: ")
        if(email_or_phone.toLower() == "email"):
            email = input("Please enter your email: ")
            break
        elif(email_or_phone.toLower() == "phone"):
            phone = input("Please enter your phone number: ")
            break
        else:
            print('Please enter either "email" or "phone" as your choice.')

    print("Account successfully created")



def password_change():
    username = input("Please enter a valid username: ")
    #check if the username exists

    #check if the account has either a email or phone number associated with it
    while(True):
        password = input("Please enter a new password: ")
        rePassword = input("Please reenter your password: ")
        if (password == rePassword):
            break
        print("Passwords did not match. Please try again")
    


def game_summary():
    print("This is a math zombie game where you use math problems to defeat evil zombies! As you play you can earn currency and buy powerups to better help you to defeat the zombies")
    



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

    
