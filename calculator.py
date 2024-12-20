def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the simple calculator!")
    
    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter the number corresponding to the operation: ")
    
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid input! Please enter a number between 1 and 4.")

# Run the calculator
calculator()
