# Simple Calculator File. Operations include adding, subtracting, multiplying, dividing,
# and raising a number to a power.


# Function to add two numbers a and b together.
def add(a, b):
    return a + b

# Function to subtract two numbers a minus b.
def subtract(a, b):
    return a - b

# Function to multiply two numbers a times b.
def multiply(a, b):
    return a * b

# Function to divide two numbers, a divided by b.
def divide(a, b):
    return a / b

# Function to raise one number to the defined power, such as a to the power of b.
def power(a, b):
    return a ** b

# Main method to access the user's input, use their choice to perform operation.
# Implemented in order to separate arithmetic operations, rather than having them altogether.
def main():
    while True:
        print("Welcome to the Super Awesome Wonderful Calculator!"
          "\nList of Options:")
        print("1. Addition"
              "\n2. Subtraction"
              "\n3. Multiplication"
              "\n4. Division"
              "\n5. Exponentiation"
              "\n6. Exit")
        choice = int(input("Please select an operation: "))
        if choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid choice, please try again.")
            continue
        elif choice == 6:
            break
        a = float(input("Please enter your first number: "))
        b = float(input("Please enter your second number: "))
        if choice == 1:
            print(a, "plus", b, "is equal to:", add(a, b))
            continue
        elif choice == 2:
            print(a, "minus", b, "is equal to:", subtract(a, b))
            continue
        elif choice == 3:
            print(a, "multiplied by", b, "is equal to:", multiply(a, b))
            continue
        elif choice == 4:
            print(a, "divided by", b, "is equal to:", divide(a, b))
            continue
        elif choice == 5:
            print(a, "raised to the", b, "power is equal to:", power(a, b))
            continue
main()


