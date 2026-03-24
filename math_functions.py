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
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        
        userAnswer = int(input(f"{num1} + {num2} = "))

        if userAnswer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

    if difficulty == "Hard":
        num1 = random.randint(99, 999)
        num2 = random.randint(999, 999)
        
        userAnswer = int(input(f"{num1} + {num2} = "))

        if userAnswer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

def subtraction_problem_easy():
    num1 = random.randint(0, 9)
    