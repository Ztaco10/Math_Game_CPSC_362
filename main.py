import math_functions
import login

def arithmetic_operations():
    arithmetic = int(input("\n*** ARITHMETIC OPERATIONS ***\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Exit\nSELECTED: "))
    # ARITHMETIC OPERATIONS -------------
    # ADDIDITION OPERATIONS ------
    if arithmetic == 1:
        print('')
        login.print_equals()
        print('')

        difficulty = int(input("*** DIFFICULTY ***\n1. Easy\n2. Medium\n3. Hard\n4. Return to Main Menu\nSELECTED: "))
        # difficulty options 1-4, 4 to exit
        
        if difficulty == 1:
            for i in range(5):
                math_functions.addition_problem("easy")
                
        elif difficulty == 2:
            for i in range(5):
                math_functions.addition_problem("medium")
                
        elif difficulty == 3:
            for i in range(5):
                math_functions.addition_problem("hard")
                
        elif difficulty == 4:
            print("*** Returning to Main Menu...")
            return
    # SUBTRACTION OPERATIONS ------
    if arithmetic == 2:

        print('')
        login.print_equals()
        print('')

        difficulty = int(input("*** DIFFICULTY ***\n1. Easy\n2. Medium\n3. Hard\n4. Return to Main Menu\nSELECTED: "))
        # difficulty options 1-4, 4 to exit
        
        if difficulty == 1:
            for i in range(5):
                math_functions.subtraction_problem("easy")
                
        if difficulty == 2:
            for i in range(5):
                math_functions.subtraction_problem("medium")
                
        if difficulty == 3:
            for i in range(5):
                math_functions.subtraction_problem("hard")
                
        if difficulty == 4:
            print("*** Returning to Main Menu...")
            return
    # MULTIPLICATION OPERATIONS ------
    if arithmetic == 3:

        print('')
        login.print_equals()
        print('')

        difficulty = int(input("*** DIFFICULTY ***\n1. Easy\n2. Medium\n3. Hard\n4. Return to Main Menu\nSELECTED: "))
        # difficulty options 1-4, 4 to exit
		
        if difficulty == 1:
            for i in range(5):
                math_functions.mul_problem("easy")
                
        if difficulty == 2:
            for i in range(5):
                math_functions.mul_problem("medium")
                
        if difficulty == 3:
            for i in range(5):
                math_functions.mul_problem("hard")
                
        if difficulty == 4:
            print("*** Returning to Main Menu...")
            return
    # part of main menu option
    if arithmetic == 4:
        print("*** Exiting program... ***")
        return


#Game Loop
#Main menu contains arithmetic operation selections from 1-4. break out of this loop when user enters 4
while True:
    print('')
    login.print_equals()
    print('')
    print('\033[1m' + "*** GAME MAIN MENU ***" + '\033[0m')
    print("1. Play Game")
    print("2. Go to Shop")
    print("3. Visit Profile")
    print("4. Exit to Login Page")
    value = 0

    try:
        choice = int(input("Enter choices 1-4: "))
        if(value != 0):
            print('')
            login.print_equals()
            print('')

        value = 1
            
        if(choice > 5 or choice < 1):
            raise ValueError
        
    except ValueError:
        print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
        value = 0

    arithmetic_operations()