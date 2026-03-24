import math_functions
while True:
    print("*** MAIN MENU ***")
    arithmetic = int(input("\n*** ARITHMETIC OPERATIONS ***\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Exit\nSELECTED: "))
    if arithmetic == 1:

        difficulty = int(input("*** DIFFICULTY ***\n1. Easy\n2. Medium\n3. Hard\n4. Return to Main Menu\nSELECTED: "))
        while True:
            if difficulty == 1:
                count = 10
                while count != 0:
                    math_functions.addition_problem("easy")
                    count -= 1
            if difficulty == 2:
                count = 10
                while count != 0:
                    math_functions.addition_problem("medium")
                    count -= 1
            if difficulty == 3:
                count = 10
                while count != 10:
                    math_functions.addition_problem("hard")
                    count-=10
            if difficulty == 4:
                print("*** Returning to Main Menu...")
                break
    if arithmetic == 4:
        print("*** Exiting program... ***")
        break
