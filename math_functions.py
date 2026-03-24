import random

def addition_problem_easy():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    userAnswer = int(input(f"{num1} + {num2} = "))

    if userAnswer == num1 + num2:
        print("Correct")
    else:
        print("Wrong")
    