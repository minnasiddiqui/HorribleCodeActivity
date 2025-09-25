#Calculator file that presents poor coding practices.

import math

def subtract(n1, n2):

    # if n1 > n2:
    #   print("First number is bigger")
    # else:
    #   print("Second number is bigger")

    a = n1
    b = n2

    return a + b

class UserProfile():
    def __init(self, name):
        self.username = name
        print(f"Profile for '{self.username}' created.")

def do_calc (p, op, x1, x2):
    if op =='+':
        return x1 + x2
    elif op == '-':
        return x1 - x2
    else:
        return 0

def run_calculator():
    profile = UserProfile()

    op_choice = input("Enter operation (+ or -): ")

    if op_choice == '+':
        print ("Please give two numbers for addition")
        val1 = float(input("Enter first value: "))
        val2 = float(input("Enter second value: "))

        result = do_calc(profile, '+', val1, val2)

        print(f"The result is ==> {result}")

    elif op_choice == '-':
        print("Please give two numbers for subtraction.")
        val1 = float(input("Enter first value: "))
        val2 = float(input("Enter second value: "))

        result = do_calc(profile, '-', val1, val2)

        print(f"The result is ==> {result}")

run_calculator()