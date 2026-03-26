import math_functions

#Game Loop
#Main menu contains arithmetic operation selections from 1-4. break out of this loop when user enters 4
while True:
    print("*** MAIN MENU ***")
    arithmetic = int(input("\n*** ARITHMETIC OPERATIONS ***\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Exit\nSELECTED: "))
    # ARITHMETIC OPERATIONS -------------
    # ADDIDITION OPERATIONS ------
    if arithmetic == 1:
        
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
            break
    # SUBTRACTION OPERATIONS ------
    if arithmetic == 2:
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
            break
    # MULTIPLICATION OPERATIONS ------
    if arithmetic == 3:
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
            break
    # part of main menu option
    if arithmetic == 4:
        print("*** Exiting program... ***")
        break
