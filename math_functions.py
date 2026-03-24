import random

def addition_problem(difficulty):
    if difficulty == "Easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        
        userAnswer = int(input(f"{num1} + {num2} = "))

        if userAnswer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

    if difficulty == "Medium":
        choice = random.randint(1, 2)
        if choice == 1:
            num1 = random.randint(0, 99)
            num2 = random.randint(0, 99)
        if choice == 2:
            num1 = random.randint(0, 99)
            num2 = random.randint(0, 999)
        
        userAnswer = int(input(f"{num1} + {num2} = "))

        if userAnswer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

    if difficulty == "Hard":
        choice = random.randint(1, 2)
        if choice == 1:
            num1 = random.randint(99, 999)
            num2 = random.randint(100, 999)
        if choice == 2:
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)

        userAnswer = int(input(f"{num1} + {num2} = "))

        if userAnswer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

def mul_problem(difficulty):
    if difficulty == "Easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        
        userAnswer = int(input(f"{num1} x {num2} = "))

        if userAnswer == num1 * num2:
            print("Correct")
        else:
            print("Wrong")

    if difficulty == "Medium":
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        
        userAnswer = int(input(f"{num1} x {num2} = "))

        if userAnswer == num1 * num2:
            print("Correct")
        else:
            print("Wrong")

    if difficulty == "Hard":
        num1 = random.randint(99, 999)
        num2 = random.randint(999, 999)
        
        userAnswer = int(input(f"{num1} x {num2} = "))

        if userAnswer == num1 * num2:
            print("Correct")
        else:
            print("Wrong")


    